# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        movies = [item['title'], item['url'], item['type'], item['release_date']]
        movies_pd = pd.DataFrame(data=movies)
        movies_pd.to_csv('./movie.csv', mode='a+', encoding='utf-8', index=False, header=False)
        return item
