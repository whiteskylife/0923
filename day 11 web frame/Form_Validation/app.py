#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import re


class IPFiled:
    REGULAR = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$" #静态 字段

    def __init__(self, error_dict=None, required=True):
        """
        :param error_dict: 显示用户错误
        :param required:   默认表示必须要填值
        """
        # 封装了错误信息  81行实例化时候封装的
        self.error_dict = {}
        if error_dict:# 81 行实例化 传入的错误信息,如果不传 则为None,则不会执行
            self.error_dict.update(error_dict) #将实例化时候 传入的错误信息封装

        self.required = required # # 81 行实例化 传入的是否为空字段,默认是浏览器输入不许为空

        self.error = None   # 错误信息
        self.value = None
        self.is_valid = False

    def validate(self, name, input_value):
        """
        :param name: 字段名
        :param input_value: 用户表单中输入的内容
        :return:
        """
        if not self.required: # 当比如81行我们传入可以为空的时候即False时候走这一段代码
            # 用户输入可以为空
            self.is_valid = True      # 设置封装值为真
            self.value = input_value  #将空值封装
        else:   #当81行要求输入不为空时候
            # 用户有输入,这一要验证正则了。
            if not input_value.strip():  # 输入为空,返回错误信息。 错误信息字典
                if self.error_dict.get('required',None):  # 81行定义的错误信息。如果未定义则自己定义
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name #默认错误信息
            else:  # 输入不为空,
                ret = re.match(IPFiled.REGULAR, input_value) #获取 静态字段的正则字符串,跟用户的input输入内容匹配
                if ret: # 匹配通过,
                    self.is_valid = True
                    self.value = input_value
                else:  #匹配不通过,返回错误字典
                    if self.error_dict.get('valid', None): #81 行定义的错误信息,如果未定义则自己定义
                        self.error = self.error_dict['valid']
                    else:
                        self.error = "%s is invalid" % name


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
        self.ip = IPField(required=True)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self, *args, **kwargs):
        obj = IndexForm()
        is_valid, value_dict = obj.check_valid(self)
        if is_valid:
            print(value_dict)


class HomeHandler(tornado.web.RequestHandler):
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
    (r"/home", HomeHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()











