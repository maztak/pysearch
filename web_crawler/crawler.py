import requests
from urllib.parse import urlparse, urljoin

from pymongo import MongoClient
from janome.tokenizer import Tokenizer
from bs4 import BeautifulSoup

from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client[urlparse(MONGO_URL).path[1:]]
col = db["Index"]


def _split_to_word(text):
    """Japanese morphological analysis with janome.
    Splitting text and creating words list.
    """
    print('split to word')
    t = Tokenizer()
    surfaces = []
    for token in t.tokenize(text):
        print('surface: ', token.surface)
        surfaces.append(token.surface)
    return surfaces


def _get_page(url):
    print('get page')
    r = requests.get(url)
    if r.status_code == 200:
        return r.text


def _extract_url_links(base_url, html):    
    print('extract url links')
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup.find_all('a')
    links = []
    for anchor in anchors:
      href = anchor.get('href')
      link = urljoin(base_url, href)
      links.append(link)
    return links

def add_to_index(keyword, url):
    entry = col.find_one({'keyword': keyword})
    if entry:
        if url not in entry['url']:
            print('add to index')
            print('keyword: ', keyword, 'url: ', url)
            entry['url'].append(url)
            col.save(entry)
        return
    # not found, add new keyword to index
    col.insert({'keyword': keyword, 'url': [url]})


def add_page_to_index(url, html):
    print('add page to index')
    body_soup = BeautifulSoup(html, "html.parser").find('body')
    for child_tag in body_soup.findChildren():
        if child_tag.name == 'script':
            continue
        child_text = child_tag.text
        for line in child_text.split('\n'):
            line = line.rstrip().lstrip()
            for word in _split_to_word(line):
                add_to_index(word, url)


def crawl_web(base_url, seed, max_depth):
    print('crawl web')
    to_crawl = {seed}
    crawled = []
    next_depth = []
    depth = 0
    while to_crawl and depth <= max_depth:
        page_url = to_crawl.pop()
        print('page_url:', page_url)
        if page_url not in crawled:
            print('crawling page url:', page_url)
            html = _get_page(page_url)
            add_page_to_index(page_url, html)
            to_crawl = to_crawl.union(_extract_url_links(base_url, html))
            crawled.append(page_url)
        if not to_crawl:
            to_crawl, next_depth = next_depth, []
            depth += 1
