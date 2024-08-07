import pymysql

# DB 연결
def db_connect():
    conn = pymysql.connect(
        host='localhost',
        user='testuser',
        password='Tkkwak0419?!',
        db='db_test',
        charset='utf8mb4',
        # 사용시 데이터 딕셔너리로 데이터가 반환됨.
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

# SQL 실행
SQL = 'SELECT * FROM tb_board' # 요청(sql)을 실행하는 부분
# with as 문 사용 : with문이 끝나면 자동으로 close()를 해준다.
# 자원 반환하는 문법이 필요한 경우에 사용
with db_connect() as conn:
    with conn.cursor() as cursor:
        cursor.execute(SQL)
        results = cursor.fetchall()
        print(results)
