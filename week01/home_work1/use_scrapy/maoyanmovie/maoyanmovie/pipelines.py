# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanmoviePipeline:
    """
        Scrapy pipeline to process data and output to csv file
    """
    def process_item(self, item, spider):
        movies = [item['title'], item['type'], item['release_date']]
        with open('./movie.csv', 'a+') as file_writer:
            file_writer.write(','.join(movies) + '\n')
        return item
