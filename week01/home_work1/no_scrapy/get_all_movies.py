"""This Python script retrieve HTML information from given site and parse it"""
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from lxml import etree, html
import pandas as pd
import argparse


def prepare_header() -> dict:
    _headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Dnt": "1",
        "Connection": "keep-alive",
        "Host": "httpbin.org",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    }
    return _headers


def parse_response(_bs_info: bs, _total_movies: int, _session: requests.Session):
    _counter, _movies = 0, []
    for tags in _bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
        if _counter < _total_movies:
            _counter += 1
            _movie_url, _movie_name = '', ''
            for atag in tags.find_all('a'):
                _movie_url = atag.get('href')
                _movie_name = atag.text
            print(_movie_url, _movie_name)
            _name, _type, _release_date = process_single_movie(_movie_url, _session)
            _movies.append([_name, _type, _release_date])
    return _movies


def process_single_movie(_movie_url, _session):
    if TEST == 'no':
        _response = _session.get(_movie_url, headers=header)
        _selector = etree.HTML(response.text.replace("<dd>", "</dd><dd>"))
    else:
        with open('./test.htm', 'rb') as f:
            _selector = html.fromstring(f.read())

    _name = _selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1')[0].text.strip()
    _release_date = _selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]')[0].text.strip()
    _type = _selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]')[0].text.strip()

    return _name, _release_date, _type


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', choices=['yes', 'no'])
    args = parser.parse_args()
    TEST = args.test

    # Define movie url and headers
    main_url = 'https://maoyan.com/films?showType=3'
    headers = prepare_header()

    # Prepare session
    # Note due to verification from maoyan, I downloaded main movie page and one example movie page
    # to local for testing purpose
    session = None
    if TEST == 'no':
        session = requests.Session()
        response = session.get(main_url, headers=headers)
        bs_info = bs(response.text, 'html.parser')
    else:
        with open('./main.htm', 'rb') as f:
            response = f.read()
        bs_info = bs(response, 'html.parser')

    movies = parse_response(bs_info, 10, session)
    
    # Write into csv file
    movies_pd = pd.DataFrame(data=movies)
    movies_pd.to_csv('./movie.csv', encoding='utf8', index=False, header=False)
