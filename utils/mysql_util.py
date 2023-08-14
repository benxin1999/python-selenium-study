import pymysql

from utils.read import read_ini
from utils.log import logger


data = read_ini()['mysql']
DB_CONF = {
    'host': data['HOST'],
    'port': int(data['PORT']),
    'user': data['USER'],
    'password': data['PASSWD'],
    'db': data['DB']
}


class MySqlDB:
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    def select_db_one(self, sql):
        logger.info(f'Executing SQL statement {sql}')
        self.cur.execute(query=sql)
        result = self.cur.fetchone()
        logger.info(f'The result of the query is "{result}"')
        return result

    def select_db_all(self, sql):
        logger.info(f'Executing SQL statement {sql}')
        self.cur.execute(query=sql)
        result = self.cur.fetchall()
        logger.info(f'The result of the query is "{result}"')
        return result

    def execute_sql(self, sql):
        try:
            logger.info(f'执行SQL:{sql}' )
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info(f"执行SQL出错:{sql}")

    def __del__(self):
        self.cur.close()
        self.conn.close()


db = MySqlDB()

if __name__ == "__main__":
    db = MySqlDB()
    mobile = '18884322941'
    print(type(mobile))
    # sql = f"select code from users_verifycode where mobile = {mobile} order by id desc limit 1;"
    sql = f'SELECT * FROM users_userprofile'
    res = db.select_db_all(sql)
    print(res)