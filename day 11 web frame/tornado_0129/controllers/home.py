#!/usr/bin/env python
# -*-coding utf-8 -*-

import tornado.ioloop
import tornado.web

LIST_INFO = [
    {'username': 'alex', 'email': 'whisky@163.com'},
]
for i in range(200):
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
        if surplus > 0:     # all_pager为页数，如果存在余数并大于0，则说明有多余的内容，总页数加一来显示，余数为0,则页数为all_pager
            all_pager += 1  # 总页数加一来显示余下内容
        list_page = []
        # 调整分页开始
        start_page = page - 5
        if start_page < 0:
            start_page = 0
        end_page = page + 5
        if end_page > all_pager:
            end_page = all_pager

        if page < 5:
            end_page = 10
        if page + 5 > all_pager:
            start_page = all_pager - 10
        # 调整分页结束
        for p in range(start_page, end_page):      # 生成HTML页码
            if p + 1 == page:           # 当p等于用户输入的页码：page时，表示处在当前页
                temp = '<a class="active" href="/index/%s">%s</a>' % (p + 1, p + 1)
            else:
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
