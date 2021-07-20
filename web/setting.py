# -*- coding: utf-8 -*-
# @File   : setting.py
# @Coder  : Einsfat
# @Date   : 2021/7/20 22:21
class AppConfig(object):
    pass


class DatabaseConfig(object):
    """
    数据库配置
    """
    SQLALCHEMY_DATABASE_URI = "sqlite:///web/data/data.sqlite3"
