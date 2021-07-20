# -*- coding: utf-8 -*-
# @File   : db_base.py
# @Coder  : Einsfat
# @Date   : 2021/7/20 22:19
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from web.setting import DatabaseConfig
from sqlalchemy import Column, Integer, BigInteger

Engine = create_engine(DatabaseConfig.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}, echo=True)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=Engine)
Base = declarative_base()


# class BaseModel(Base):
#     __abstract__ = True
#     id = Column(Integer, primary_key=True, index=True, nullable=False, comment="id")
#     create_time = Column(BigInteger, nullable=False, comment="create_time")
#     update_time = Column(BigInteger, nullable=False, comment="update_time")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    try:
        Base.metadata.create_all(bind=Engine, checkfirst=True)
    except Exception as e:
        print(e)
        raise
