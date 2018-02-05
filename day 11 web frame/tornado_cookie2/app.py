#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument('u', None) in ['whisky', 'alex']:
            self.set_cookie('name', self.get_argument('u'))
        else:
            self.write('请登录')


class ManagerHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie('name', None) in ['whisky', 'alex']:
            self.write('欢迎登录：' + self.get_cookie('name'))
        else:
            self.redirect('/index')


settings = {
    'template_path': 'views',
    'static_path': 'statics'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()