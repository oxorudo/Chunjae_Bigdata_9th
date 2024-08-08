from flask import Flask

app = Flask(__name__)


# 기본 주소 :  http://127.0.0.1:5000/
# '/' : 주소 뒤에 아무것도 입력하지 않았을 때 이 함수 호출
@app.route("/")
def index():
    return "Hello World!"


# '/asdf' :  http://127.0.0.1:5000/asdf 로 접속하면 위의 함수 대신 이 함수로 이동
@app.route("/asdf")
def hello_world():
    return "Hello World!!!!!!!!"


# 동적 라우팅
# 주소의 일부분을 변수화(<변수명>)
# 변수화 된 저 데이터를 파라미터로 받을 수 있음
@app.route("/user/<user_name>")
def hello_user_name(user_name):
    return "Hello %s" % user_name

# 동적 라우팅을 사용할 때 자료형을 정해줄 수 있다.
# 만약에 url을 옳게 입력했음에도 자료형이 다르면 404 not found가 뜬다.
@app.route("/user/by_id/<int:user_id>") # int형만 취급
def get_user_by_id(user_id: int):
    return "유저 데이터를 받아왔습니다. %s" % user_id

if __name__ == "__main__":
    app.run()
