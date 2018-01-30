#!/usr/bin/env python
# -*-coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import time


# render中的文件不要加/等路径

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        print(self.get_argument('username'))
        print(self.get_argument('password'))
        self.write('ok')    #write方法作用相当于console.log()

settings = {
    "template_path": "views",  # 模板路径配置(存放HTML)
    # 'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh' # 加密cookie的盐
}

# 路由映射，路由系统
application = tornado.web.Application([
    (r"/login", LoginHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
