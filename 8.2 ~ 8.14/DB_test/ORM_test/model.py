from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime
from sqlalchemy import String

# 이 클래스를 상속받아 DB와 내 클래스들을 연결
class Base(DeclarativeBase):
    # 빈 클래스
    pass

class User(Base):
    # 클래스명과 실제 테이블명이 다를 경우 작성
    __tablename__ = "tb_user"
    
    # mapped_column은 컬럼의 특이사항을 지정
    # PK거나, str 자료형의 길이 등을 지정
    id: Mapped[int] = mapped_column(primary_key=True)
    login_id: Mapped[str] = mapped_column(String(20))
    login_password: Mapped[str] = mapped_column(String(20))
    name: Mapped[str] = mapped_column(String(20))
    address: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    error_count: Mapped[int]
    create_date: Mapped[datetime.datetime]
    update_date: Mapped[datetime.datetime]