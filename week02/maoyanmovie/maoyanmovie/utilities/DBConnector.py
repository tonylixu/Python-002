import pymysql


class DBConnector(object):
    def __init__(self, db_info):
        self.host = db_info['DATABASE_HOST']
        self.port = db_info['DATABASE_PORT']
        self.user = db_info['DATABASE_USER']
        self.password = db_info['DATABASE_PASSWORD']
        self.db = db_info['DATABASE_NAME']

    def create_db_connection(self) -> pymysql.connect:
        """ Create a MySQL DB connection

        :return: DB connection
        """
        conn = pymysql.connect(
            host=self.host, port=self.port,
            user=self.user, password=self.password, db=self.db
        )
        return conn

    def insert_movie(self, conn, movie_info):
        # Create a database cursor
        try:
            with conn.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `movies` (`name`, `url`, `date`, `type`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, movie_info)
            conn.commit()

            with conn.cursor() as cursor:
                sql = "SELECT * FROM movies"
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
        'DATABASE_NAME': 'maoyan'
    }
    db = DBConnector(db_info)
    db_connection = db.create_db_connection()
    movie = ('test', 'http://test.org', 'test', 'test')
    db.insert_movie(db_connection, movie)
