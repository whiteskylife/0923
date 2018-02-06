#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument('u', None) in ['whisky', 'alex']:     # 设置u值默认为None，否则访问不带u参数会报400错误
            self.set_cookie('name', self.get_argument('u'))
            self.write('登录成功')
        else:
            self.write('请登录')       # 省去写前端页面，直接在前端页面输出write方法中的内容


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
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()


# 登录测试：http://127.0.0.1:8000/index?u=whisky


