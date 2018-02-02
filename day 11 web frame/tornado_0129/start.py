#!/usr/bin/env python
# -*-coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from controllers import home

# render中的文件不要加/等路径

settings = {
    "template_path": "views",  # 模板路径配置(存放HTML)
    "static_path": 'statics',    # 注册引入jQuery的静态目录
}

# 路由映射，路由系统，正则匹配输入的url（有分组时，分组的组名传给类），交给对应的类处理
application = tornado.web.Application([
    (r"/index/(?P<page>\d*)", home.IndexHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
