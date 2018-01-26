#!/usr/bin/env python
# -*-coding:utf-8 -*-

import tornado.ioloop
import tornado.web

# render中的文件不要加/等路径


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        val = self.get_cookie('auth')
        if val == '1':
            self.render('manager.html')
        else:
            print('-----------')
            self.redirect('/login')


class LoginHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('login.html', status_text='')

    def post(self, *args, **kwargs):
        username = self.get_argument('username', None)
        pwd = self.get_argument('password', None)
        if username == 'alex' and pwd == '123':
            self.set_cookie('auth', '1')
            self.redirect('/manager')
        else:
            self.render('login.html', status_text='登录失败')


class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('auth', '0')
        self.redirect('/login')


settings = {
    "template_path": "views",        # 模板路径配置(存放HTML)
}

# 路由映射，路由系统
application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/login", LoginHandler),
    (r"/manager", ManagerHandler),
    (r"/logout", LogoutHandler),

], **settings)


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
