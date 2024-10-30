# import pymysql
# import db.pgsql_query as mysql_query

# from settings import DB_SETTINGS
# from sqlalchemy import create_engine


# class DBConnector:
#     def __init__(self, engine, orm_engine,host, database, user, password, port):
#         self.engine = engine
#         self.orm = orm_engine
#         self.conn_params = {
#             "host": host,
#             "user": user,
#             "password": password,
#             "database": database,
#             "port": port
#         }
#         self.orm_conn_params = f"{orm_engine}://{user}:{password}@{host}:{port}/{database}"
#         self.orm_connect()
        
#         if self.engine == 'mysql+pymysql':
#             self.connect = self.mysql_connect()
#             self.queries = mysql_query.queries
        
#     def __enter__(self):
#         print("Enter")
#         return self
    
#     def __exit__(self, exe_type, exe_value, traceback):
#         # self.conn.close()
#         print("Exit")
        
#     def orm_connect(self):
#         self.orm_conn = create_engine(self.orm_conn_params)
#         return self.orm_conn
        
#     def mysql_connect(self):
#         self.conn = pymysql.connect(**self.conn_params)
#         return self
    
#     def get_query(self, table_name):
#         try:
#             _query = self.queries[table_name]
#             return _query
#         except KeyError:
#             raise KeyError(f"'{table_name}' 키가 queries 에 존재하지 않습니다. {list(self.queries.keys)}")

import pymysql
import db.pgsql_query as mysql_query
from settings import DB_SETTINGS
from sqlalchemy import create_engine


class DBConnector:
    def __init__(self, engine, orm_engine, host, database, user, password, port):
        self.engine = engine
        self.orm = orm_engine
        self.conn_params = dict(
            host= host,
            user = user,
            password= password,
            database =  database,
            port = int(port)
        )
        self.orm_conn_params = f"{orm_engine}://{user}:{password}@{host}:{port}/{database}"
        self.orm_conn = self.orm_connect()
        self.conn = None  # conn 초기화

        if self.engine == 'mysql+pymysql':
            self.connect = self.mysql_connect()
            self.queries = mysql_query.queries  # self.queries 초기화
        else:
            self.queries = mysql_query.queries  # 기본값으로 빈 딕셔너리 설정

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exe_type, exe_value, traceback):
        if hasattr(self, 'conn') and self.conn:  # conn 속성 확인 및 존재 여부 체크
            self.conn.close()
        print("Exit")

    def orm_connect(self):
        self.orm_conn = create_engine(self.orm_conn_params)
        return self.orm_conn

    def mysql_connect(self):
        self.conn = pymysql.connect(**self.conn_params)
        return self

    def get_query(self, table_name):
        try:
            _query = self.queries[table_name]
            # print(_query)
            return _query
        except KeyError:
            raise KeyError(f"'{table_name}' 키가 queries에 존재하지 않습니다. {list(self.queries.keys())}")
