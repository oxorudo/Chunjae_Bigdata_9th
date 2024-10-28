import os

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
    "KDT9": {
        'host': os.getenv("POSTGRES_HOST"),
        'database': os.getenv("POSTGRES_DB_2"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'port': os.getenv("POSTGRES_PORT")
    }
}