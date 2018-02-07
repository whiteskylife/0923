#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web

# 把session封装为一个类，开发时无需关注生成字符串、设置cookie等细节，直接设置session的key和value即可，注意：代码中cookie的key是写死的

container = {}
# container = {
#     '第一个人的随机字符串': {},
#     '第二个人的随机字符串': {'k1': 111, 'parents': '你'},
# }


class Session:
    def __init__(self, handler):
        """
        :param handler: 传进来的IndexHandler对象，具有了set_cookie方法
        """
        self.handler = handler

    def __generate_random_str(self):
        # 生成加密串,方法只能在类里面调用
        import hashlib
        import time
        obj = hashlib.md5()
        obj.update(bytes(str(time.time()), encoding='utf-8'))
        random_str = obj.hexdigest()  # 根据时间生成随机字符串
        return random_str

    def set_value(self, key, value):
        """
        :param key: 定义session的key
        :param value: 定义session的value
        :return:
        """
        # 在container中加入随机字符串
        # 定义session属于各自用户数据
        # 在客户端中写入随机字符串
        # 判断请求的用户是否第一次请求，是否已有随机字符串
        random_str = self.__generate_random_str()
        container[random_str] = {}  # 创建专属于自己的session数据空间为一个空字典
        container[random_str][key] = value
        self.handler.set_cookie("___kakaka___", random_str)  # cookie的key定义要统一记准，值为random_str

    def get_value(self, key):
        """
        :param key:传入session的key
        :return: 返回session的value
        """
        # 获取客户端的随机字符串
        # 从container中获取专属于我的数据
        random_str = self.handler.get_cookie("___kakaka___", None)
        print(random_str)
        user_info_dict = container[random_str]
        value = user_info_dict[key]
        return value


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument('u', None) in ['whisky', 'alex']:     # 设置u值默认为None，否则访问不带u参数会报400错误
            s = Session(self)
            s.set_value('is_login', True)   # 初始化创建session的key和value
        else:
            self.write('请用正确的用户名登录')


class ManagerHandler(tornado.web.RequestHandler):
    def get(self):
        s = Session(self)
        val = s.get_value('is_login')
        if val:
            self.write('登录成功')
        else:
            self.write('失败')
settings = {
    'template_path': 'views',
    'static_path': 'statics'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()


# 登录测试：http://127.0.0.1:8000/index?u=whisky


