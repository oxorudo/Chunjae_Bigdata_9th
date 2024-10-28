import psycopg2
import db.pgsql_query as postgresql_query
from settings import DB_SETTINGS
from sqlalchemy import create_engine


class DBConnector:
    def __init__(self, engine, orm_engine, host, database, user, password, port):
        self.engine = engine
        self.orm_engine = orm_engine
        self.conn_params = dict(
            host = host,
            dbname = database,
            user = user,
            password = password,
            port = port
        )
        self.orm_conn_params = f'{orm_engine}://{user}:{password}@{host}:{port}/{database}'
        self.orm_connect()

        if self.engine == 'postgresql':
            self.connect = self.postgres_connect()
            self.queries = postgresql_query.queries
        # elif self.engine == 'mysql' : ...

    def __enter__(self):
        print("enter")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        print('exit')

    def orm_connect(self):
        self.orm_conn = create_engine(self.orm_conn_params)

    def postgres_connect(self):
        self.conn = psycopg2.connect(**self.conn_params)
        return self
    
    def get_query(self, table_name):
        try:
            _query = self.queries[table_name]
            return _query
        except KeyError:
            raise KeyError(f'{table_name} 키가 query에 존재하지 않습니다. 현재 있는 키 리스트 : {list(self.queries.keys())}')