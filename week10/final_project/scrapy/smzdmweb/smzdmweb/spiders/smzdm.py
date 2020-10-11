# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.selector import Selector
from smzdmweb.items import SmzdmwebItem

class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/diannaoyouxi/']

    def start_requests(self):
        """Override the start_requests method of
        the spider to make it carry cookies
        """
        settings = get_project_settings()
        cookies = settings.get('COOKIES')
        for url in self.start_urls:
            yield scrapy.Request(url=url, cookies=cookies, callback=self.parse)

    def parse(self, response):
        """Get product details directly from the landing page"""
        url_prefix = 'https://www.smzdm.com'
        products = Selector(response=response).xpath('//*[@id="feed-main-list"]/li')
        for product in products[:2]:
            item = SmzdmwebItem()
            url = product.xpath('div/div[2]/h5/a/@href').extract()[0]
            item['product_url'] = url
            title = product.xpath('div/div[2]/h5/a/text()').extract()[0]
            item['product_title'] = title
            item['product_type'] = 'Game'
            # yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_single_product)

    @staticmethod
    def parse_single_product(response):
        pass
        # item = response.meta['item']
        # movie_details = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        # for detail in movie_details:
        #     item['movie_title'] = detail.xpath('./h1/text()').extract_first().strip()
        #     item['movie_release_date'] = detail.xpath('./ul/li[3]/text()').extract_first().strip()[:10]
        #     movie_type = [str(t.extract()).strip() for t in detail_.xpath('./ul/li[1]/a/text()')]
        #     item['movie_type'] = '/'.join(movie_type)
        #     yield item
