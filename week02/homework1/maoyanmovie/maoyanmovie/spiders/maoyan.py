# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem

# Check proxy IPs
TEST = False


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com', 'httpbin.org']
    start_urls = ['http://httpbin.org/ip'] if TEST else ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        """Override the start_requests method of
        the spider to make it carry cookies
        """
        settings = get_project_settings()
        cookies = settings.get('COOKIES')
        for url in self.start_urls:
            yield scrapy.Request(url=url, cookies=cookies, callback=self.parse)

    def parse(self, response):
        """Get movie details directly from the landing page"""
        url_prefix = 'https://maoyan.com'
        movies = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
        for movie in movies[:10]:
            item = MaoyanmovieItem()
            url = url_prefix + movie.xpath('./a/@href').extract()[0]
            item['movie_url'] = url
            print(item['movie_url'])
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_single_movie)

    @staticmethod
    def parse_single_movie(response):
        item = response.meta['item']
        movie_details = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        for detail in movie_details:
            item['movie_title'] = detail.xpath('./h1/text()').extract_first().strip()
            item['movie_release_date'] = detail.xpath('./ul/li[3]/text()').extract_first().strip()[:10]
            movie_type = [str(t.extract()).strip() for t in detail_.xpath('./ul/li[1]/a/text()')]
            item['movie_type'] = '/'.join(movie_type)
            yield item
