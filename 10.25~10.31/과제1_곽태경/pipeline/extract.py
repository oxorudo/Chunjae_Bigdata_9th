import pandas as pd
import db.pgsql_query

def extractor(db_connector, table_name):
    with db_connector as connected:
        try:
            _query = connected.get_query(table_name)
            con = connected.orm_connect()
            if con is None:
                raise ValueError("데이터베이스 연결이 설정되지 않았습니다.")
            
            df = pd.read_sql(_query, con)
            return df
        except Exception as e:
            print(f"Extract MSG: {e}")
            return pd.DataFrame()  # 빈 데이터프레임 반환
