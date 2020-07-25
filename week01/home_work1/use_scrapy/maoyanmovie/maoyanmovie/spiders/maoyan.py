# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from maoyanmovie.items import MaoyanmovieItem


class MaoyanSpider(scrapy.Spider):
    """
        Use beautifulsoup to parse movie HTML page and retrieve movie info
    """
    name, allowed_domains = 'maoyan', ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.\
            find('dl', attrs={'class': 'movie-list'}).\
            find_all('div', attrs={'class': 'movie-hover-info'})
        counter = 0
        for movie in movies:
            if counter < 10:
                item = MaoyanmovieItem()
                movie_title = movie.find('span', attrs={'class': 'name'}).text.strip()
                # extract all the strings as some of them have no tags at all
                m_strings = [s.strip() for s in movie.find_all(string=True)]
                type_idx = m_strings.index('类型:') + 1
                time_idx = m_strings.index('上映时间:') + 1
                movie_type, movie_release_date = m_strings[type_idx], m_strings[time_idx]
                # Save into items
                item['title'], item['type'], item['release_date'] = movie_title, movie_type, movie_release_date
                yield item
            counter += 1
