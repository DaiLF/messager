# -*- coding: utf-8 -*-
# @File   : db_base.py
# @Coder  : Einsfat
# @Date   : 2021/7/20 22:19
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from web.setting import DatabaseConfig

engine = create_engine(DatabaseConfig.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}, echo=True)
Base = declarative_base()


def get_db() -> None:
    """
    获取数据库连接\n
    :return: None
    """
    session_factory = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    db_session = scoped_session(session_factory)
    try:
        yield db_session
    finally:
        db_session.close()


def init_db() -> None:
    """
    初始化数据库\n
    :return: None
    """
    try:
        Base.metadata.create_all(bind=engine, checkfirst=True)
    except Exception as e:
        print(e)
        raise
