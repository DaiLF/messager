# -*- coding: utf-8 -*-
# @File   : views.py.py
# @Coder  : Einsfat
# @Date   : 2021/7/23 17:22
from fastapi import APIRouter
from starlette.requests import Request
from web.app import templates

router = APIRouter()


@router.get("/message", tags=["Mobile"])
async def message(request: Request):
    return templates.TemplateResponse("mobile/index.html", {"request": request})
