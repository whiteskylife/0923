#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import re


class BaseForm:
    def check_valid(self, handle):
        """
         获取用户提交的数据，将用户提交的数据和正则表达式匹配
        :param handle: post方法中的self，里面封装了get_argument方法，可以直接取前端传过来的参数值
        :return:返回正则匹配结果：成功-True；失败：false
        """
        flag = True
        value_dict = {}
        for key, regular in self.__dict__.items():    # 遍历self中封装的参数
            # key是host、ip、port、phone
            input_value = handle.get_argument(key)      # input_value是获取用户输入的内容
            # print(input_value, regular)
            val = re.match(regular, input_value)
            if not val:  # 有一个或n个正则匹配失败
                flag = False
            value_dict[key] = input_value
        return flag, value_dict


class IndexForm(BaseForm):
    def __init__(self):
        self.host = "(.*)"
        self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"
        self.port = '(\d+)'
        self.phone = '^1[3|4|5|8][0-9]\d{8}$'


class HomeForm(BaseForm):
    def __init__(self):
        self.host = "(.*)"
        self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self, *args, **kwargs):
        obj = IndexForm()
        is_valid, value_dict = obj.check_valid(self)
        if is_valid:
            print(value_dict)


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()











