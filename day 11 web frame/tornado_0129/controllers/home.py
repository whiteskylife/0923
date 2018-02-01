#!/usr/bin/env python
# -*-coding utf-8 -*-

import tornado.ioloop
import tornado.web

LIST_INFO = [
    {'username': 'alex', 'email': 'whisky@163.com'},
    {'username': 'alex', 'email': 'whisky@163.com'},
    {'username': 'alex', 'email': 'whisky@163.com'},
    {'username': 'alex', 'email': 'whisky@163.com'},
    {'username': 'alex', 'email': 'whisky@163.com'},
    {'username': 'alex', 'email': 'whisky@163.com'},
    {'username': 'alex', 'email': 'whisky@163.com'},
]


class IndexHandler(tornado.web.RequestHandler):

    def get(self, page):
        # print(nid)
        # self.write('ok')
        try:
            page = int(page)
        except:
            page = 1
        if page < 1:
            page = 1
        # if page > len(LIST_INFO):
        #     page =
        start = (page - 1) * 5
        end = page * 5
        current_list = LIST_INFO[start:end]
        self.render('home/index.html', list_info=current_list)

    def post(self, page):
        user = self.get_argument('username')
        email = self.get_argument('email')
        temp = {'username': user, 'email': email}
        LIST_INFO.append(temp)
        self.redirect('/index/')
