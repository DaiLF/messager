# -*- coding: utf-8 -*-
# @File   : app.py
# @Coder  : Einsfat
# @Date   : 2021/7/14 23:08
from fastapi import FastAPI
from typing import Optional


def register_router(app: FastAPI) -> None:
    """
    集中注册路由\n
    :param app: FastAPI 实例
    :return: None
    """
    from web.work.view import router as work_router
    app.include_router(work_router)
    return None


def create_app() -> FastAPI:
    """
    工厂模式创建 FastAPI 实例\n
    :return: FastAPI()
    """
    app = FastAPI()
    register_router(app)
    return app
