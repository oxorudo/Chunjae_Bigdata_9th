from flask import (
    Flask,
    abort,
    g,
    redirect,
    render_template,
    session,
    request,
    flash,
    url_for,
    jsonify
)
from db.connection import db_connect

# 플라스크 사용
app = Flask(__name__)

# from_object() 는 인자로 주어진 객체를 설정값을 읽어 오기 위해 살펴 볼 것이다.
# 모듈 이름을 통해 파이썬 파일을 서치하는데, __name__을 직접 넣으면 현재 파일을 바라본다.
# 사용자가 입력한 정보와 비교하기 위해서 유저네임과 비밀번호 정보를 찾는다.
app.config.from_object('db.db_config.Config')
# db 폴더 안의 db_config 파일 안의 Config 함수를 가져온다.

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


@app.route("/")
def show_entries():
    sql = """
            SELECT title, text 
            FROM entries 
            ORDER BY id DESC
            """

    entries = []
    with g.conn.cursor() as cur:
        cur.execute(sql)
        entries = cur.fetchall()
    # render_template는 플라스크 안에 있음
    return render_template("show_entries.html", entries=entries)


# 하고싶은 것 : 우리의 Flask는 지금 HTML만 받는다.
# HTML뿐만 아니라 json이라고 하는 데이터 형태로 response를 전달하고 싶다.
@app.route('/api/entries')
def json_entries():
    sql = '''
            SELECT id, title, text
            FROM entries
            ORDER BY id DESC
            '''
    
    entries = []
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            entries = cur.fetchall()

    # 파이썬이 가지고 있는 튜플, 리스트, 데이터 딕셔너리를
    # json 문법에 맞게(배열, 자바스크립트 객체)로 변경해 준다.
    return jsonify(entries)

# 실습
@app.route("/entries")
def view_entries():
    # 0. 데이터베이스나 지금 이 사이트를 이용하여 데이터를 추가합니다.
    # 1. 이 라우터가 빈 HTML을 반환하도록 한다.
    # 2. js에서 fetch()를 이용해서 entries 데이터를 호출하도록 한다.
    # 3. js를 이용하여 화면에 entries의 제목들이 나오도록 해 봅시다.
    return render_template('show_data.html')

# methods=[POST] : POST 요청만 받는다는 뜻
@app.route("/add", methods=["POST"])
def add_entry():
    # session은 서버의 임시 공간인데, 주로 유저 정보를 저장한다.
    if not session.get("logged_in"):
        # 요청에 대한 거절이다.
        abort(401)
    
    sql = """
            INSERT INTO entries(
            title,text
            ) values (
            %s, %s
            )
            """
    
    with g.conn.cursor() as cur:
        # request는 유저의 요청에 대한 정보를 담고 있음
        # request 내부에는 데이터를 저장하고 있는 form이라는 객체가 있음 (POST일 때만)
        cur.execute(sql, [request.form["title"], request.form["text"]])
    g.conn.commit()
    # flash : 메시지 띄우는 용도
    flash("New entry was successfully posted")
    # redirect는 다른 화면으로 보내는 함수
    # url_for는 함수 이름으로 연결된 route를 찾는다.(여기서는 show_entries의 '/')
    return redirect(url_for("show_entries"))


# GET, POST : GET과 POST 요청을 다 받는다.
@app.route('/login', methods=['GET',"POST"])
def login():
    error = None
    if request.method == 'POST':
        # 유저의 요청 안에 유저명/비밀번호를 체크
        if request.form['username'] != app.config['USERNAME']:
            error = 'INVALID USERNAME!!'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'INVALID PASSWORD!!'
        else:
            # 로그인에 성공했으면 session에 logged_in이 들어간다.
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    # 로그인 html을 보여준다.
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    # pop() 메서드는 해당 키에 있는 데이터를 제거
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == "__main__":
    app.run()
