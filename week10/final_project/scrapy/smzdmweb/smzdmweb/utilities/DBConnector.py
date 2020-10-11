import pymysql


class DBConnector(object):
    def __init__(self, db_info):
        self.host = db_info['DATABASE_HOST']
        self.port = db_info['DATABASE_PORT']
        self.user = db_info['DATABASE_USER']
        self.password = db_info['DATABASE_PASSWORD']

    def create_db_host_connection(self) -> pymysql.connect:
        """ Create a MySQL DB connection
        :return: DB connection
        """
        conn = pymysql.connect(
            host=self.host, port=self.port,
            user=self.user, password=self.password
        )
        return conn

    def create_db_connection(self, database: str) -> pymysql.connect:
        """ Create a MySQL DB connection for a given database
        :return: DB connection
        """
        conn = pymysql.connect(
            host=self.host, port=self.port,
            user=self.user, password=self.password, db=database
        )
        return conn

    def create_database_utf8(self, name: str):
        """Create a new database in utf-8 format
        :param conn: database connection
        :param name: database name
        :return:
        """
        conn = self.create_db_host_connection()
        try:
            with conn.cursor() as cursor:
                sql = f"CREATE DATABASE IF NOT EXISTS `{name}` CHARACTER SET utf8 COLLATE utf8_general_ci"
                cursor.execute(sql)
        except:
            print(f'[Error]: Create database {name} failed')
            conn.rollback()
        finally:
            conn.close()

    def create_products_table(self, db_name: str, table_name: str='products'):
        """Create products table
        :param db_name: Database name
        :param table_name: table name
        :return:
        """
        conn = self.create_db_connection(db_name)
        try:
            with conn.cursor() as cursor:
                sql = f'CREATE TABLE IF NOT EXISTS {table_name}(title TEXT, url TEXT, type TEXT, comment TEXT)'
                cursor.execute(sql)
        except:
            print(f'[Error]: Create table {table_name} in {db_name} failed')
            conn.rollback()
        finally:
            conn.close()

    def create_products_review_table(self, db_name: str, table_name: str='products_review'):
        """Create products table
        :param db_name: Database name
        :param table_name: table name
        :return:
        """
        conn = self.create_db_connection(db_name)
        try:
            with conn.cursor() as cursor:
                sql = f'CREATE TABLE IF NOT EXISTS {table_name}(title TEXT, comment TEXT, star INT)'
                cursor.execute(sql)
        except:
            print(f'[Error]: Create table {table_name} in {db_name} failed')
            conn.rollback()
        finally:
            conn.close()

    def insert_product(self, db_name: str, product_info: tuple):
        """Insert a product into database table
        :param db_name: database name
        :param product_info: product info in tuple format
        """
        # Create a database cursor
        conn = self.create_db_connection(db_name)
        try:
            with conn.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `products` (`title`, `url`, `type`, `comment`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, product_info)
            conn.commit()

            with conn.cursor() as cursor:
                sql = "SELECT * FROM products"
                cursor.execute(sql)
                print([row for row in cursor.fetchall()])
        except:
            conn.rollback()
        finally:
            conn.close()


if __name__ == '__main__':
    db_info = {
        'DATABASE_HOST': '127.0.0.1',
        'DATABASE_PORT': 3306,
        'DATABASE_USER': 'root',
        'DATABASE_PASSWORD': 'root',
    }
    db = DBConnector(db_info)
    db.create_database_utf8('smzdm')
    db.create_products_table('smzdm')
    db.create_products_review_table('smzdm')
    product = ('test', 'test', 'test', 'test')
    db.insert_product('smzdm', product)
