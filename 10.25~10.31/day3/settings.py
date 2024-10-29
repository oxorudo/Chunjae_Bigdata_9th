import os

TEMP_PATH = 'd:\\workspace\\Chunjae_Bigdata_9th\\10.25~10.31\\day3\\temp_storage'

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
        'host': os.getenv("MYSQL_HOST"),
        'database': os.getenv("MYSQL_DB_2"),
        'user': os.getenv("MYSQL_USER"),
        'password': os.getenv("MYSQL_PASSWORD"),
        'port': os.getenv("MYSQL_PORT")
    }
}