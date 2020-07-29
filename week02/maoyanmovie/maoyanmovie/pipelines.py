# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
from .utilities import DBConnector
import yaml


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        #self.save_to_db(item, spider)
        self.save_to_csv(item, spider)
        return item

    @staticmethod
    def open_db_yaml_file(file_name: str='db_settings.yml') -> dict:
        """Open DB config yaml for read

        :param file_name: DB config file name, default db_settings.yml
        :return: db_info dictionary
        """
        with open(file_name, 'r') as file_reader:
            yaml_content = yaml.load(file_reader, Loader=yaml.FullLoader)
        return yaml_content['database_settings']

    def save_to_db(self, item, spider):
        db_info = MaoyanmoviePipeline.open_db_yaml_file()
        db = DBConnector.DBConnector(db_info)
        db_connection = db.create_db_connection()
        movie = (item['title'], item['url'], item['release_date'], item['type'])
        db.insert_movie(db_connection, movie)
        return item

    def save_to_csv(self, item, spider):
        print("Save item to csv")
        movies = [item['title'], item['url'], item['type'], item['release_date']]
        movies_pd = pd.DataFrame(data=movies)
        movies_pd.to_csv('./movie.csv', mode='a+', encoding='utf-8', index=False, header=False)
        return item
