# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanmovieItem(scrapy.Item):
    # Define tile, url release_date and type for movie
    movie_title = scrapy.Field()
    movie_url = scrapy.Field()
    movie_release_date = scrapy.Field()
    movie_type = scrapy.Field()
