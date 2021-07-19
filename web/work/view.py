# -*- coding: utf-8 -*-
# @File   : view.py
# @Coder  : Einsfat
# @Date   : 2021/7/14 23:16
from fastapi import APIRouter

router = APIRouter()


@router.get("/index", tags=["Home"])
async def index() -> dict:
    message = {
        "msg": "Hello, World !"
    }
    return message
