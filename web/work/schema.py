# -*- coding: utf-8 -*-
# @File   : schema.py
# @Coder  : xyp_s
# @Date   : 2021/7/21 21:01
from pydantic import BaseModel


class Base(BaseModel):
    id: int = None
    create_time: int = None
    update_time: int = None
