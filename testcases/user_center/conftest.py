from utils.log import logger
from utils.mysql_util import db


def delete_user(mobile):
    sql = f'delete from users_userprofile where username = {mobile}'
    db.execute_sql(sql)

def get_code(mobile):
    sql =  f"select code from users_verifycode where mobile = {mobile} order by id desc limit 1;"
    code = db.select_db_one(sql)['code']
    return code