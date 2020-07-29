import pymysql


class DBConnector(object):
    def __init__(self, db_info, sqls):
        self.host = db_info['DATABASE_HOST']
        self.port = db_info['DATABASE_PORT']
        self.user = db_info['DATABASE_USER']
        self.password = db_info['DATABASE_PASSWORD']
        self.db = db_info['DATABASE_NAME']
        self.sqls = sqls

    def run(self, result):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )

        # Create a database cursor
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        conn.close()


if __name__ == '__main__':
    db = DBConnector(sqls)
    result = []
    db.run(result)
    print(result)
