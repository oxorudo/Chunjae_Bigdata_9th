import os
from dotenv import load_dotenv
import os

# .env 파일의 경로를 명시적으로 지정할 수 있습니다.
load_dotenv('./.env')

TEMP_PATH = 'd:\\workspace\\Chunjae_Bigdata_9th\\10.25~10.31\\day2\\temp_storage'

DB_SETTINGS = {
    "POSTGRES": {
        'engine' : os.getenv('POSTGRES_ENGINE'),
        'orm_engine' : os.getenv('POSTGRES_ENGINE'),
        'host': os.getenv("POSTGRES_HOST"),
        'database': os.getenv("POSTGRES_DB"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'port': os.getenv("POSTGRES_PORT")
    },
"MYSQL": {
        'engine': os.getenv('MYSQL_ENGINE', 'mysql+pymysql'),  # pymysql을 기본 엔진으로 설정
        'orm_engine': os.getenv('MYSQL_ENGINE', 'mysql+pymysql'),
        'host': os.getenv("MYSQL_HOST"),
        'database': os.getenv("MYSQL_DB_2"),
        'user': os.getenv("MYSQL_USER"),
        'password': os.getenv("MYSQL_PASSWORD"),
        'port': int(os.getenv("MYSQL_PORT", 3306))  # 기본 포트로 3306 설정
    }
}