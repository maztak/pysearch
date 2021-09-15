import requests
from urllib.parse import urlparse, urljoin
from web_crawler.crawler import crawl_web
from bs4 import BeautifulSoup

def _get_page(url):
    print('get page')
    r = requests.get(url)
    if r.status_code == 200:
        return r.text

def _extract_url_links(base_url, html):
    """extract url links

    >>> _extract_url_links('aa<a href="link1">link1</a>bb<a href="link2">link2</a>cc')
    ['link1', 'link2']
    """
    print('extract url links')
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup.find_all('a')
    print('anchors: ', anchors)
    links = []
    for anchor in anchors:
      href = anchor.get('href')
      link = urljoin(base_url, href)
      links.append(link)
    print('links: ', links)
    return links

def crawl_web(base, seed, max_depth):
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
            to_crawl = to_crawl.union(_extract_url_links(base, html))
            crawled.append(page_url)
        if not to_crawl:
            to_crawl, next_depth = next_depth, []
            depth += 1
  
if __name__ == '__main__':
    crawl_web('https://docs.sphinx-users.jp/', 'https://docs.sphinx-users.jp/contents.html', 1)