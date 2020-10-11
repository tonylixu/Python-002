import pandas as pd
from utilities import DBConnector
from scrapy.utils.project import get_project_settings


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


if __name__ == '__main__':
    database = 'smzdm'
    # Get login credentials from settings.py and login
    db_info = get_db_settings()
    db = DBConnector.DBConnector(db_info)
    db_conn = db.create_db_connection(database)

    # Define statement
    df = pd.read_sql('SELECT * FROM products;', db_conn)
    print(df[0])