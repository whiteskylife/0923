#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import re


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')

    def post(self, *args, **kwargs):
        val = self.request.files.get('fafafa', [])   # 注意checkbox必须用get_arguments，加s的参数
        # val = self.request.files['fafafa']   # 注意checkbox必须用get_arguments，加s的参数
        print(type(val), val)
        # 当提交一个文件时：输出 <class 'list'> [{'content_type': 'text/plain', 'body': b'1', 'filename': 'app.py'}]
        # 两个文件输出：
        # <class 'list'> [{'filename': 'app.py', 'body': b'1', 'content_type': 'text/plain'},
        # {'filename': 'app1.py', 'body': b'2', 'content_type': 'text/plain'}]
        # 提交空输出：   <class 'list'> []


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/'
}

application = tornado.web.Application([
    (r"/home", IndexHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()

