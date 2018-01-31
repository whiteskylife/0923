#!/usr/bin/env python
# -*-coding utf-8 -*-

import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):

    def get(self, nid):
        print(nid)
        self.write('ok')
        self.render('home/index.html')
