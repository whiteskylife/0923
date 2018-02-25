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
        print(type(val), val)                          # 输出 ['2', '3']


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

