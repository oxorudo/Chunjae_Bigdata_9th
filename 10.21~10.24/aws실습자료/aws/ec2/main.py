from flask import Flask, render_template, request, redirect, url_for, send_file
import boto3
from botocore.exceptions import NoCredentialsError
import json
from dotenv import load_dotenv
import os 
import io
import pymysql


# .env 파일에서 환경 변수 로드
load_dotenv()

ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
S3_REGION = os.getenv('region')
# Flask 애플리케이션 생성
app = Flask(__name__)

# # AWS S3 관련 설정
S3_BUCKET = 'your_bucket_name'


# AWS S3 클라이언트 생성
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)


# MySQL 데이터베이스 연결 설정
def get_db_connection():
    connection = pymysql.connect(
        host='rds엔드포인트',       # 데이터베이스 서버 주소
        user='유저이름',   # 사용자 이름
        password='비밀번호', # 사용자 비밀번호
        database='db 이름',        # 데이터베이스 이름
        charset='utf8mb4',      # 문자 인코딩
        cursorclass=pymysql.cursors.DictCursor  # 커서 클래스 설정 (선택 사항)
    )
    return connection



# index 화면을 제공할 라우트
@app.route('/')
def index():
    return render_template('index.html')



# 파일 업로드 폼을 제공할 라우트
@app.route('/s3')
def s3_upload():
    return render_template('s3upload.html')


# 파일 업로드 처리를 수행할 라우트
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # 업로드할 파일 가져오기
        file = request.files['file']

        if file:
            try:
                # S3에 파일 업로드
                s3.upload_fileobj(file, S3_BUCKET, file.filename)
                return redirect(url_for('index'))
            except NoCredentialsError:
                return 'AWS credentials not available.'
    return 'File upload failed.'


# 데이터 분석 결과 페이지를 제공할 라우트
@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')



@app.route('/get_image')
def get_image():
    file_key = 'student_visualization.png'
    local_file_path = os.path.join('static', file_key)
    try:
        # S3에서 파일 가져오기
        file_obj = s3.get_object(Bucket=S3_BUCKET, Key=file_key)
        file_content = file_obj['Body'].read()
        # print(file_content)
        with open(local_file_path, 'wb') as f:
            f.write(file_content)

        # 이미지를 응답으로 전송
        return send_file(io.BytesIO(file_content), mimetype='image/png', as_attachment=False, download_name='student_visualization.png')
    except Exception as e:
        return str(e)



# 4. RDS 사용해보기
@app.route('/db_page')
def db_page():
    return render_template('insert_db.html')

@app.route('/select_rds')
def select_rds():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, name, email FROM test_table"
            cursor.execute(sql)
            results = cursor.fetchall()
    finally:
        connection.close()
    return render_template('show_db.html', results=results)


@app.route('/insert_rds', methods=['POST'])
def insert_rds():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        connection = get_db_connection()
        try:
            # 데이터베이스와 상호 작용하는 코드
            with connection.cursor() as cursor:
                # INSERT 쿼리 실행
                sql = "INSERT INTO test_table (name, email) VALUES (%s, %s)"
                values = (name, email)
                cursor.execute(sql, values)
            
            # 변경사항 저장
            connection.commit()

        finally:
            # 연결 닫기
            connection.close()
        
        return redirect('/select_rds')




# 웹 서버 실행
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
