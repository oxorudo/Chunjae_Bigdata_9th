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
SQL = '''INSERT INTO 
            tb_board(title, content, user_id)
        values
            (%s, %s, %s)
'''
# with as 문 사용 : with문이 끝나면 자동으로 close()를 해준다.
# 자원을 다 쓰고 반환해야 하는 경우에 사용
with db_connect() as conn:
    with conn.cursor() as cursor:
        board = ('python에서 쓴 제목','python에서 쓴 내용', 3)
        cursor.execute(SQL, board)
        conn.commit()