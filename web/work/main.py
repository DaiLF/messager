# -*- coding: utf-8 -*-
# @File   : main.py
# @Coder  : Einsfat
# @Date   : 2021/7/14 23:18
from sqlalchemy.orm import Session
from web.work.model import User


def add_user(db: Session, name: str, role: int) -> None:
    try:
        db_user = User(name="Einsfat", role=0)
        db.add(db_user)
        db.commit()
        db.flush()
    except Exception:
        db.rollback()


def get_user(db: Session) -> dict:
    result = {}
    try:
        query_data = db.query(User).all()
        for item in query_data:
            result.update({
                "id": item.id,
                "name": item.name,
                "role": item.role
            })
    except Exception as e:
        pass
    return result
