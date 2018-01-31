#!/usr/bin/env python
# -*-coding utf-8 -*-

import tornado.ioloop
import tornado.web


class LoginHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write('ok')


class LogoutHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write('ok')


class RegisterHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write('ok')
