# -*- coding: utf-8 -*-
# @File   : run.py.py
# @Coder  : Einsfat
# @Date   : 2021/7/14 23:21
import uvicorn

from web.app import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(app="run:app")
