import pymysql
import os
from pymysql.cursors import DictCursor

# 환경변수 가져오기
db_password = os.environ["db_password"]
db_host = os.environ["db_host"]
db_user = os.environ["db_user"]
db_database = os.environ["db_database"]

def get_db_connection():
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database,
        charset="utf8",
        cursorclass=DictCursor
    )
    return connection
