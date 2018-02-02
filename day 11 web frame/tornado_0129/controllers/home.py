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


class Pagination:
    def __init__(self, current_page, all_item, n):
        """
        :param current_page:  当前页
        :param total_page: 总页数
        :param n: 每页显示n条数据
        """
        # 定义总页数
        self.n = n
        all_pager, surplus = divmod(all_item, self.n)  # 每页显示5条数据
        if surplus > 0:     # all_pager为页数，如果存在余数并大于0，则说明有多余的内容，总页数加一来显示，余数为0,则页数为all_pager
            all_pager += 1  # 总页数加一来显示余下内容
        self.total_page = all_pager
        try:
            current_page = int(current_page)
        except:
            current_page = 1
        if current_page < 1:
            current_page = 1

        self.current_page = current_page

    @property
    def start(self):
        # 根据当前页取5条数据，确定每页显示的信息数目
        return (self.current_page - 1) * self.n

    @property
    def end(self):
        # 根据当前页取5条数据，确定每页显示的信息数目
        return self.current_page * self.n

    def page_str(self, base_url):
        """
        :param base_url: 自定义路径 格式: /path/
        :return:
        """
        # 调整分页开始, 固定显示十个页码号
        start_page = self.current_page - 5
        if start_page < 0:
            start_page = 0
        end_page = self.current_page + 5
        if end_page > self.total_page:
            end_page = self.total_page

        if self.current_page < 5:
            end_page = 10
        if self.current_page + 5 > self.total_page:
            start_page = self.total_page - 10
        # 调整分页结束

        list_page = []
        for p in range(start_page, end_page):        # 生成HTML页码
            if p + 1 == self.current_page:           # 当p等于用户输入的页码：page时，表示处在当前页
                temp = '<a class="active" href="%s%s">%s</a>' % (base_url, p + 1, p + 1)
            else:
                temp = '<a href="%s%s">%s</a>' % (base_url, p+1, p+1)
            list_page.append(temp)
        str_page = "".join(list_page)
        return str_page


class IndexHandler(tornado.web.RequestHandler):
    # 路由系统来调用这个类
    def get(self, page):

        page_obj = Pagination(page, len(LIST_INFO), 5)          # 传入当前输入页和总页数,每页显示信息数

        current_list = LIST_INFO[page_obj.start:page_obj.end]   # page_obj 返回，每页应该显示的信息数目
        str_page = page_obj.page_str('/index/')

        self.render('home/index.html', list_info=current_list, current_page=page_obj.current_page,
                    str_page=str_page)

    def post(self, page):
        # 这个page是从前端html中传过来的
        user = self.get_argument('username')
        email = self.get_argument('email')
        temp = {'username': user, 'email': email}
        LIST_INFO.append(temp)
        self.redirect('/index/' + str(page))
