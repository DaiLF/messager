# -*- coding: utf-8 -*-
# @File   : view.py
# @Coder  : Einsfat
# @Date   : 2021/7/14 23:16
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from web.common.db.db_base import get_db
from .main import add_user, get_user

router = APIRouter()


@router.get("/index", tags=["Home"])
async def index() -> dict:
    message = {
        "msg": "Hello, World !"
    }
    return message


@router.get("/user", tags=["Home"])
async def user(db: Session = Depends(get_db)) -> dict:
    try:
        result = get_user(db)
        return {"msg": "成功", "result": result}
    except Exception:
        return {"msg": "失败", "result": result}


@router.post("/user", tags=["Home"])
async def user(db: Session = Depends(get_db)) -> dict:
    pass
