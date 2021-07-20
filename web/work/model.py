# -*- coding: utf-8 -*-
# @File   : model.py
# @Coder  : Einsfat
# @Date   : 2021/7/14 23:18
from sqlalchemy import Column, String, Integer
from web.common.db.db_base import Base


class User(Base):
    """
    用户信息
    """
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(255), index=True)
    role = Column(Integer, index=True)

    def to_dict(self) -> dict:
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return result
