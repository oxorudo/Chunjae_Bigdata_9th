import pymysql
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from db_config import Config
from model import User

pymysql.install_as_MySQLdb()

engine = create_engine(f"mariadb+pymysql://{Config.USERNAME}:{Config.PASSWORD}@{Config.HOST}:3306/{Config.DB}?charset=utf8mb4")
session = Session(engine)

# 실제 ORM 작성 방법이다.
# 이 문장은 Database statement를 반환한다. > 쿼리 정보
stmt = select(User).where(User.login_id == 'admin')

# scalars : fetchall과 같음
users = session.scalars(stmt)

for user in users:
    print(user.id, user.login_id, user.login_password)



