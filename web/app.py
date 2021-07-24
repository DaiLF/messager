# -*- coding: utf-8 -*-
# @File   : app.py
# @Coder  : Einsfat
# @Date   : 2021/7/14 23:08
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from web.common.db.db_base import init_db

templates = Jinja2Templates(directory="web/templates")


def register_router(app: FastAPI) -> None:
    """
    集中注册路由\n
    :param app: FastAPI 实例
    :return: None
    """
    from web.work.view import router as work_router
    app.include_router(work_router)
    from web.mobile.views import router as mobile_router
    app.include_router(mobile_router)
    return None


def create_app() -> FastAPI:
    """
    工厂模式创建 FastAPI 实例\n
    :return: FastAPI()
    """
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="web/static"), name="static")
    init_db()
    register_router(app)
    return app
