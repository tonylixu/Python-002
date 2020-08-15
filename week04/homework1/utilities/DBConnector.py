# -*- coding: utf-8 -*-
"""Database utility helper"""
import pymysql
import random
import string


class DBConnector(object):
    def __init__(self, db_info):
        self.host = db_info['DATABASE_HOST']
        self.port = db_info['DATABASE_PORT']
        self.user = db_info['DATABASE_USER']
        self.password = db_info['DATABASE_PASSWORD']

    def create_db_host_connection(self) -> pymysql.connect:
        """ Create a MySQL DB host connection

        :return: DB connection
        """
        _conn = pymysql.connect(
            host=self.host, port=self.port,
            user=self.user, password=self.password
        )
        return _conn

    def create_db_connection(self, _database: str) -> pymysql.connect:
        """ Create a MySQL DB connection for a given database

        :param _database: database name
        :return: DB connection
        """
        _conn = pymysql.connect(
            host=self.host, port=self.port,
            user=self.user, password=self.password, db=_database
        )
        return _conn

    def create_database_utf8(self, _conn: pymysql.connect, _name: str):
        """Create a new database in utf-8 format

        :param _conn: database connection
        :param _name: database name
        :return:
        """
        try:
            with _conn.cursor() as _cursor:
                _sql = f"CREATE DATABASE IF NOT EXISTS `{_name}` CHARACTER SET utf8 COLLATE utf8_general_ci"
                _cursor.execute(_sql)
        except:
            print(f'[Error]: Create database {_name} failed')
            _conn.rollback()

    def create_data_table(self, _conn: pymysql.connect, _table_name: str = 'data'):
        """Create the data table

        :param _conn: Database connection
        :param _table_name: table name, default 'data'
        :return:
        """
        try:
            with _conn.cursor() as _cursor:
                _sql = f'CREATE TABLE IF NOT EXISTS {_table_name}(' \
                      f'id INT AUTO_INCREMENT PRIMARY KEY, ' \
                      f'name TEXT, age INT)'
                _cursor.execute(_sql)
        except:
            print(f'[Error]: Create table {_table_name} failed')
            _conn.rollback()

    def insert_random_data_into_data_table(self, _conn: pymysql.connect):
        """Insert some random data into data table

        :param _conn: database connection
        """
        try:
            with _conn.cursor() as _cursor:
                for _ in range(100):
                    # Create a new record
                    _letters = string.ascii_lowercase
                    _name = ''.join(random.choice(_letters) for i in range(6))
                    _age = random.randint(20, 50)
                    _sql = "INSERT INTO `data` (`name`, `age`) VALUES (%s, %s)"
                    _cursor.execute(_sql, [_name, _age])
                _conn.commit()
        except:
            _conn.rollback()

    def create_data1_table(self, _conn: pymysql.connect, _table_name: str = 'data1'):
        """ Create data1 table for testing

        :param _conn: database connection
        :param _table_name: default data1
        :return:
        """
        try:
            with _conn.cursor() as _cursor:
                _sql = f'CREATE TABLE IF NOT EXISTS {_table_name}(' \
                      f'id TEXT, order_id TEXT, cost FLOAT)'
                _cursor.execute(_sql)
        except:
            print(f'[Error]: Create table {_table_name} failed')
            _conn.rollback()

    def create_data2_table(self, _conn: pymysql.connect, _table_name: str = 'data2'):
        """Create data2 table for testing

        :param _conn: database connection
        :param _table_name: default data2
        :return:
        """
        try:
            with _conn.cursor() as _cursor:
                _sql = f'CREATE TABLE IF NOT EXISTS {_table_name}(' \
                      f'id TEXT, order_id TEXT, name TEXT)'
                _cursor.execute(_sql)
        except:
            print(f'[Error]: Create table {_table_name} failed')
            _conn.rollback()

    def insert_random_data_into_data1_table(self, _conn: pymysql.connect):
        """Insert data into data1 table

        :param _conn: database connection
        """
        with open('./data1.txt', 'r') as f_in:
            _all_sql_statements = f_in.readlines()
        try:
            with _conn.cursor() as _cursor:
                for _sql in _all_sql_statements:
                    _cursor.execute(_sql)
                    _conn.commit()
        except:
            _conn.rollback()

    def insert_random_data_into_data2_table(self, _conn: pymysql.connect):
        """Insert data into data1 table

        :param _conn: database connection
        """
        with open('./data2.txt', 'r') as f_in:
            _all_sql_statements = f_in.readlines()
        try:
            with _conn.cursor() as _cursor:
                for _sql in _all_sql_statements:
                    _cursor.execute(_sql)
                    _conn.commit()
        except:
            _conn.rollback()

    def run_given_database_query(self, _db_name: str, _sql: str, _conn: pymysql.connect) -> list:
        """Run given sql statement"""
        try:
            with _conn.cursor() as _cursor:
                _cursor.execute(_sql)
                return _cursor.fetchall()
        except:
            _conn.rollback()


if __name__ == '__main__':
    db_info = {
        'DATABASE_HOST': '127.0.0.1',
        'DATABASE_PORT': 3306,
        'DATABASE_USER': 'root',
        'DATABASE_PASSWORD': 'root',
    }
    # Create database
    db = DBConnector(db_info)
    host_conn = db.create_db_host_connection()
    db.create_database_utf8(host_conn, 'testdb')

    # Get database connection and create tables
    conn = db.create_db_connection('testdb')
    db.create_data_table(conn)
    db.create_data1_table(conn)
    db.create_data2_table(conn)
    # Insert data into tables
    db.insert_random_data_into_data_table(conn)
    db.insert_random_data_into_data1_table(conn)
    db.insert_random_data_into_data2_table(conn)
