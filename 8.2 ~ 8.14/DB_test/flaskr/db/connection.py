import pymysql
import pymysql.cursors
from db.db_config import Config

def db_connect():
    conn = pymysql.connect(
        host=Config.HOST,
        user=Config.USERNAME,
        password=Config.PASSWORD,
        db="db_test",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    
    return conn
