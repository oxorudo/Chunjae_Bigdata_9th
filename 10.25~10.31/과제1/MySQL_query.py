import mysql.connector  # MySQL Connector 추가
import psycopg2  # PostgreSQL 용
import db.pgsql_query as postgresql_query
from sqlalchemy import create_engine
from settings import DB_SETTINGS

class DBconnector:
    def __init__(self, engine, orm_engine, host, database, user, password, port):
        self.engine = engine
        self.orm_engine = orm_engine
        self.conn_params = dict(
            host=host,
            dbname=database,
            user=user,
            password=password,
            port=port
        )
        self.orm_conn_params = f"{orm_engine}://{user}:{password}@{host}:{port}/{database}"
        self.orm_connect()
        # PostgreSQL 연결 처리
        if self.engine == 'postgresql':
            self.connect = self.postgres_connect()
            self.queries = postgresql_query.queries
        # MySQL 연결 처리 추가
        elif self.engine == 'mysql':
            self.connect = self.mysql_connect()
            # MySQL 전용 쿼리 파일 생성 후 import 필요
            # import db.mysql_query as mysql_query
            # self.queries = mysql_query.queries
    def __enter__(self):
        print("Enter")
        return self
    def __exit__(self, exe_type, exe_value, traceback):
        self.conn.close()
        print("Exit")
    def orm_connect(self):
        self.orm_conn = create_engine(self.orm_conn_params)
    # PostgreSQL 연결 함수
    def postgres_connect(self):
        self.conn = psycopg2.connect(**self.conn_params)
        return self
    # MySQL 연결 함수 추가
    def mysql_connect(self):
        self.conn = mysql.connector.connect(**self.conn_params)
        return self
    # 쿼리 가져오기 함수
    def get_query(self, table_name):
        try:
            _query = self.queries[table_name]
            return _query
        except KeyError:
            raise KeyError(f"'{table_name}' 키가 queries에 존재하지 않습니다. 현재 있는 키 리스트 : {list(self.queries.keys())}")
