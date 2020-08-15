# -*- coding: utf-8 -*-
"""This python script translate and verifies MySQL statements to Pandas statements"""
# Import third party lib
import pretty_errors
from python_settings import settings
import settings as my_local_settings
import pandas as pd
import pymysql
# Import local lib
from utilities import DBConnector


def read_db_settings_from_file() -> dict:
    """Read DB connection info from file

    :return: _db_info as Python dictionary
    """
    _db_info = {}
    _db_info['DATABASE_HOST'] = settings.DATABASE_HOST
    _db_info['DATABASE_PORT'] = settings.DATABASE_PORT
    _db_info['DATABASE_USER'] = settings.DATABASE_USER
    _db_info['DATABASE_PASSWORD'] = settings.DATABASE_PASSWORD
    return _db_info


def compare_results_one(_key: str, _sql_results: list, _df: pd.DataFrame, _statements: dict):
    """Print both mysql and pandas statement for comparison for data table

    :param _key: The index of the sql statement
    :param _sql_results: SQL command results
    :param _df: Pandas dataframe for data table
    :param _statements: SQL statements in dict format
    :return:
    """
    print(f'{"#" * 40}')
    if key == '1':
        print(f'{_statements[_key]}')
        for _row in _sql_results: print(_row)
        print(f'{"-"*40}\npandas')
        print(_df.values)
    elif key == '2':
        print(f'{_statements[_key]}')
        for _row in _sql_results: print(_row)
        print(f'{"-" * 40}\npandas')
        print(_df.values[:10])
    elif key == '3':
        print(f'{_statements[_key]}')
        for _row in _sql_results: print(_row)
        print(f'{"-" * 40}\npandas')
        print(_df[['id']])
    elif key == '4':
        print(f'{_statements[_key]}')
        for _row in _sql_results: print(_row)
        print(f'{"-" * 40}\npandas')
        print(_df.shape[0])
    elif key == '5':
        print(f'{_statements[_key]}')
        for _row in _sql_results: print(_row)
        print(f'{"-" * 40}\npandas')
        _id_condition, _age_condition = _df['id'] < 1000, _df['age'] > 30
        print(_df[_id_condition & _age_condition])


def compare_results_two(_key: str, _sql_results: list, _df1: pd.DataFrame, _df2: pd.DataFrame, _statements: dict):
    """Print both mysql and pandas statement for comparison for data1 and data2 table

    :param _key: The index of the sql statement
    :param _sql_results: SQL command results
    :param _df1: Pandas dataframe for data1 table
    :param _df2: Pandas dataframe for data2 table
    :param _statements: SQL statements in dict format
    :return:
    """
    print(f'{"#" * 40}')
    if key == '6':
        print(f'{_statements[_key]}')
        for _row in _sql_results: print(_row)
        print(f'{"-" * 40}\npandas')
        print(_df1.groupby('id').aggregate({'order_id': 'count'}))
    if key == '7':
        print(f'{_statements[_key]}')
        for _row in _sql_results: print(_row)
        print(pd.merge(_df1, _df2, on='id'))
    if key == '8':
        print(f'{_statements[_key]}')
        for _row in _sql_results: print(_row)
        print(pd.concat([_df1, _df2]))
    if key == '9':
        print(f'{_statements[_key]}')
        for _row in _sql_results: print(_row)
        print(f'{"-" * 40}\npandas')
        index_names = _df1[_df1['id'] == 'CA001'].index
        _df1.drop(index_names, inplace=True)
        print(_df1.values)
    if key == '10':
        print(f'{_statements[_key]}')
        # '10': 'ALTER TABLE data1 DROP COLUMN column_name;'
        print(f'{"-" * 40}\npandas')
        print(_df1.drop(columns=['cost']))


if __name__ == '__main__':
    database = 'testdb'
    # Get login credentials from settings.py and login
    settings.configure(my_local_settings)
    db_info = read_db_settings_from_file()
    db = DBConnector.DBConnector(db_info)
    db_conn = db.create_db_connection(database)

    # Test statement 1 ~ 5
    statements = settings.STATEMENTS_ONE
    df = pd.read_sql('select * from data;', db_conn)
    # Load table data into pandas
    for key, sql in statements.items():
        sql_results = db.run_given_database_query(database, sql, db_conn)
        compare_results_one(key, sql_results, df, statements)

    # Test statement 6 ~ 10
    statements = settings.STATEMENTS_TWO
    df1 = pd.read_sql('select * from data1;', db_conn)
    df2 = pd.read_sql('select * from data2;', db_conn)
    for key, sql in statements.items():
        sql_results = db.run_given_database_query(database, sql, db_conn)
        compare_results_two(key, sql_results, df1, df2, statements)
