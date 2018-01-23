#!/usr/bin/env python
# -*-coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


application = tornado.web.Application([
    (r"/index", MainHandler),
])

#下面做了两件事：1.创建socket对象；2.循环socket对象。内部用了epoll，select，IO多路复用
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()