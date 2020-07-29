# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem

TEST = False


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com', 'httpbin.org']
    start_urls = ['http://httpbin.org/ip'] if TEST else ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        if TEST:
            print(response.text)
            return
        url_prefix = 'https://maoyan.com'
        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        counter = 0
        for movie in movies:
            # Only interested in the first 10 movies
            if counter < 10:
                item = MaoyanmovieItem()
                movie_url = url_prefix + movie.xpath('./a/@href').extract_first().strip()
                item['url'] = movie_url
                yield scrapy.Request(url=movie_url, meta={'item': item}, callback=self.parse_single_movie)
            counter += 1

    def parse_single_movie(self, response):
        item = response.meta['item']
        movie_title = Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
        movie_type = Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[1]/text()')
        movie_release_date = Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
        item['title'] = movie_title.extract_first().strip()
        item['release_date'] = movie_release_date.extract_first().strip()
        item['type'] = movie_type.extract_first().strip()
        yield item
