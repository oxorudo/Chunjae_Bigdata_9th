from flask import Flask, g
from db import db_connect

# 플라스크 사용
app = Flask(__name__)

# 예를 들어 /user 라는 요청이 왔을 때
# /user에 해당하는 라우터를 실행하기 전에
# 데이터베이스에 미리 커넥션을 연결
@app.before_request
def before_request():
    g.conn = db_connect()

# /user에서 라우터의 함수 실행이 끝난 후(요청에 대한 응답을 보내준 후)
# 데이터베이스의 커넥션을 종료
@app.teardown_request
def teardown_request(exception):
    g.conn.close()