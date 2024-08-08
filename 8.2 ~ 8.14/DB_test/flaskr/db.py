import pymysql
import pymysql.cursors
from db_config import HOST, USER, PASSWORD

def db_connect():
    conn = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db="db_test",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    
    return conn

