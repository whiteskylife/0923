#!/usr/bin/env python
# -*-coding utf-8 -*-

from core inport Handler

class IndexHandler(Handler.MyHandler):

    def get(self, *args, **kwargs):
        print('456')
        self.render('extend/index.html', list_info=[1, 22, 33])

    def post(self, *args, **kwargs):
        pass


class FuckoffHandler(Handler.MyHandler):
    def get(self, *args, **kwargs):
        self.render('extend/fuck.html', list_info=[11, 22, 33])


