#!/usr/bin/env python
# -*-coding:utf-8 -*-

import tornado.ioloop
import tornado.web


# 处理请求的类:
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render('s1.html')

    def post(self, *args, **kwargs):
        self.write("Hello, world")


settings = {
    "template_path": "tpl",        # 模板路径配置
    'static_path': 'static',       # 静态文件指定路径
}

# 路由映射，路由系统
application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)

# 下面做了两件事：1.创建socket对象；2.循环socket对象。内部用了epoll，select，IO多路复用
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
