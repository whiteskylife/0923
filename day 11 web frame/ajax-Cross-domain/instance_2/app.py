#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        callback = self.get_argument('callback')
        self.write('%s([11,22,33]);' % callback)

    def post(self, *args, **kwargs):
        self.write('t2.post')


class CorsHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('{"status":1, "message": "get"}')

    def post(self, *args, **kwargs):
        self.write('{"status":1, "message": "post"}')


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
    application.listen(8002)
    tornado.ioloop.IOLoop.instance().start()
