# -*- coding: utf-8 -*-
# @File   : model.py
# @Coder  : Einsfat
# @Date   : 2021/7/14 23:18
from sqlalchemy import Column, TIMESTAMP, String, Integer, BigInteger, func

from web.common.db.db_base import Base


class BaseModel(Base):
    """
    基础Model模型对象
    """
    __abstract__ = True
    id = Column(BigInteger, primary_key=True, index=True, doc='序号')
    create_time = Column(TIMESTAMP, nullable=False, server_default=func.now(), doc='创建时间')
    update_time = Column(TIMESTAMP, nullable=False, server_default=func.now(), doc='更新时间')


class User(BaseModel):
    """
    用户信息
    """
    __tablename__ = "t_user"

    name = Column(String(255), nullable=False, index=True)
    role = Column(Integer, nullable=False, index=True)

    def to_dict(self) -> dict:
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return result
