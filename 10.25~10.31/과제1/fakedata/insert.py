import pandas as pd
from db.connector import DBConnector
from settings import DB_SETTINGS


def insert_fakedataframe(df: pd.DataFrame) -> bool:
    db_connector = DBConnector(**DB_SETTINGS['MYSQL'])
    print(db_connector)

    with db_connector as connected:
        try:
            orm_conn = connected.orm_connect()
            df.to_sql(name = 'fake', con = orm_conn, if_exists = 'append', index = False)
            return True
        
        except Exception as e:
            print(e)
            return False