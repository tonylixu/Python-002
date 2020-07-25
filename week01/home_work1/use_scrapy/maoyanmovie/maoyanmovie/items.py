# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanmovieItem(scrapy.Item):
    """
        Define movie item fields
    """
    title = scrapy.Field()
    release_date = scrapy.Field()
    type = scrapy.Field()
