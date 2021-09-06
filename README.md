# Search Engine and Web Crawler in Python

![Screenshot](https://qiita-image-store.s3.amazonaws.com/0/29989/786c36ad-4de7-43a7-75a0-98c82e412fa3.png "Screenshot")

- Implement a web crawler
- japanese morphological analysis using [janome](https://github.com/mocobeta/janome)
- Implement search engine
- Store in MongoDB
- Web frontend using [Flask](http://flask.pocoo.org/)

More details are avairable from [My Tech Blog(Japanese)](http://nwpct1.hatenablog.com/entry/python-search-engine).

## Requirements

- Python 3.5

## Setup

1. Clone repository

    ```
    $ git clone git@github.com:mejiro/SearchEngine.git
    ```
    
2. Install python packages

    ```
    $ cd SearchEngine
    $ pip3 install -r requirements.txt -c constraints.txt
    ```

3. MongoDB settings

    Install MongoDB
    ```
    $ 
    ```

    Install pymongo
    ```
    $
    ```

    Start mongo shell and create table(e.g. index table)
    ```
    $ mongo
    > use index
    ```

    in `config.py`, set the mongo url, like below.

    ```
    MONGO_URL = 'mongodb://127.0.0.1:27017/index'
    ```

    If you want to use MongoDB with GUI, I recommend free software [Robo 3T](https://robomongo.org/). Only Robo 3T is sufficient(No Studio 3T is needed).

4. Run

    ```
    $ python3 manage.py crawler # build a index
    $ python3 manage.py webpage # access to http://127.0.0.1:9000
    ```
