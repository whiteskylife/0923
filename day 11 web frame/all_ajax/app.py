#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self, *args, **kwargs):
        print(self.get_argument('k1'))
        self.write('{"status": 1, "message": "mmm"}')


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
