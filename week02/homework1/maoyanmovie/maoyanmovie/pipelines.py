# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
from .utilities import DBConnector
from scrapy.utils.project import get_project_settings


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        self.save_to_db(item, spider)
        #self.save_to_csv(item, spider)
        return item

    @staticmethod
    def get_db_settings() -> dict:
        """Open DB config yaml for read

        :param file_name: DB config file name, default db_settings.yml
        :return: db_info dictionary
        """
        db_info = {}
        settings = get_project_settings()
        db_info['DATABASE_HOST'] = settings.get('DATABASE_HOST')
        db_info['DATABASE_PORT'] = settings.get('DATABASE_PORT')
        db_info['DATABASE_USER'] = settings.get('DATABASE_USER')
        db_info['DATABASE_PASSWORD'] = settings.get('DATABASE_PASSWORD')
        return db_info

    def save_to_db(self, item, spider):
        db_info = MaoyanmoviePipeline.get_db_settings()
        db = DBConnector.DBConnector(db_info)
        database_name = 'maoyan'
        db.create_database_utf8(database_name)
        db.create_movies_table(database_name)
        movie = (item['movie_title'], item['movie_url'], item['movie_release_date'], item['movie_type'])
        db.insert_movie(database_name, movie)
        return item

    def save_to_csv(self, item, spider):
        print("Save item to csv")
        movies = [item['movie_title'], item['movie_url'], item['movie_type'], item['movie_release_date']]
        movies_pd = pd.DataFrame(data=movies)
        movies_pd.to_csv('./movie.csv', mode='a+', encoding='utf-8', index=False, header=False)
        return item
