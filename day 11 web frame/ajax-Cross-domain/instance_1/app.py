#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self, *args, **kwargs):
        self.write('t1.post')


class CorsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('cors.html')

    def post(self, *args, **kwargs):
        self.write('t1.post')


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/cors", CorsHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()

