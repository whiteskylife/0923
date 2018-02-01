#!/usr/bin/env python
# -*-coding utf-8 -*-

import tornado.ioloop
import tornado.web

LIST_INFO = [
    {'username': 'alex', 'email': 'whisky@163.com'},
]
for i in range(99):
    temp_dic = {'username': 'alex'+str(i), 'email': str(i) + '123@qq.com'}
    LIST_INFO.append(temp_dic)


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
        all_pager, surplus = divmod(len(LIST_INFO), 5)
        if surplus > 0:
            all_pager += 1
        list_page = []
        for p in range(all_pager):
            temp = '<a href="/index/%s">%s</a>' % (p+1, p+1)
            list_page.append(temp)
        str_page = "".join(list_page)

        self.render('home/index.html', list_info=current_list, current_page=page, str_page=str_page)

    def post(self, page):
        # 这个page是从前端html中传过来的
        user = self.get_argument('username')
        email = self.get_argument('email')
        temp = {'username': user, 'email': email}
        LIST_INFO.append(temp)
        self.redirect('/index/' + str(page))
