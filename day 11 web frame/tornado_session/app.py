#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web

# 结合session实现的验证码，每个用户登录生成验证码，保存到用户对应的session中
container = {}
# container = {
#     '第一个人的随机字符串': {},
#     '第二个人的随机字符串': {'k1': 111, 'parents': '你'},
# }


class Session:
    def __init__(self, handler):
        """
        :param handler: 即是：Session(self)中的self，是传进来的IndexHandler对象，具有了set_cookie方法
        """
        self.handler = handler
        self.random_str = None

    def __generate_random_str(self):
        # 生成加密串,方法只能在类里面调用
        import hashlib
        import time
        obj = hashlib.md5()
        obj.update(bytes(str(time.time()), encoding='utf-8'))
        random_str = obj.hexdigest()  # 根据时间生成随机字符串
        return random_str

    def __setitem__(self, key, value):
        """
        :param key: 定义session用户信息的key
        :param value: 定义session用户信息的value
        :return:
        """
        # 在container中加入随机字符串
        # 定义session属于各自用户数据
        # 在客户端中写入随机字符串
        # 创建随机字符串之前，应该判断请求的用户是否第一次请求、第一次登录，是否已有随机字符串
        if not self.random_str:
            random_str = self.handler.get_cookie("___kakaka___")
            if not random_str:
                random_str = self.__generate_random_str()
                # self.handler.set_cookie("___kakaka___", random_str)  # 不存在随机字符串时，认为不存在cookie，此处需设置cookie；
                # 如存在random_str，则认为存在cookie，if条件下面无需再次设置cookie。cookie的key定义要统一记准，值为random_str
                container[random_str] = {}  # 创建专属于自己的session数据空间为一个空字典
            else:
                # 客户端有随机字符串
                if random_str in container.keys():
                    pass
                else:                           # 此种情况发生在服务器端重启时，浏览器端有random_str,服务器端没有，则重新生成random_str
                    random_str = self.__generate_random_str()
                    container[random_str] = {}
            self.random_str = random_str
        # 定义session的key和value
        container[self.random_str][key] = value
        self.handler.set_cookie("___kakaka___", self.random_str)
        # 生产开发中，如果没有定义cookie超时时间，此处不需设置cookie，如果设置了cookie超时时间，到了时间之前再次访问时，应该重新写一次cookie，相当于延长一下超时时间，否则原来的cookie到了超时时间则过期

    def __getitem__(self, key):
        """
        :param key:传入session用户信息的key
        :return: 返回session用户信息的value
        """
        # 获取客户端的随机字符串
        # 从container中获取专属于我的数据
        random_str = self.handler.get_cookie("___kakaka___", None)
        if not random_str:      # 没有随机字符串表示没有登录
            return None
        # 客户端有random_str：
        user_info_dict = container.get(random_str, None)
        if not user_info_dict:          # 服务器端没有random_str对应的值（服务器端可能重启过），返回空
            return None
        value = user_info_dict.get(key, None)
        return value


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):                       # initialize是RequestHandler类中初始化最后执行的方法
        self.session = Session(self)          # self.session对象中封装session；Session(self)：传递self对象是为了在Session类中可以调用set_cookie方法


class IndexHandler(BaseHandler):
    def get(self):                       # 此处self会默认传递给父类、基类
        if self.get_argument('u', None) in ['whisky', 'alex']:     # 设置u值默认为None，否则访问不带u参数会报400错误
            # s = Session(self)                                 # 传递self对象是为了在Session类中可以调用set_cookie方法
            # self.session.set_value('is_login', True)               # 初始化创建session的key和value
            # self.session.set_value('name', self.get_argument('u', None))
            self.session['is_login'] = True
            self.session['name'] = self.get_argument('u', None)
            print(container)
        else:
            self.write('请用正确的用户名登录')


class ManagerHandler(BaseHandler):
    def get(self):
        # s = Session(self)                 # 传递self对象是为了在Session类中可以调用set_cookie方法
        # val = self.session.get_value('is_login')
        val = self.session['is_login']
        if val:
            # self.write(self.session.get_value('name'))
            self.write(self.session['name'])
        else:
            self.write('失败')


class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html', status='')

    def post(self, *args, **kwargs):
        user = self.get_argument('user', None)
        pwd = self.get_argument('pwd', None)
        code = self.get_argument('code', None)
        check_code = self.session['CheckCode']
        try:
            if code.upper() == check_code.upper():
                self.write('验证码正确')
            else:
                # self.redirect('/index')
                self.render('index.html', status='验证码错误')
        except:
            print('验证码错误')
            self.write('验证码错误')
            self.render('index.html')


class CheckCodeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        # 生成图片并返回
        import io
        import check_code
        mstream = io.BytesIO()      # 相当于内存中临时创建了一个文件
        img, code = check_code.create_validate_code()       # 创建图片，并写入验证码
        img.save(mstream, "GIF")
        # 通过session为每个用户保存其验证码
        self.session["CheckCode"] = code
        self.write(mstream.getvalue())              # 返回图片内容


settings = {
    'template_path': 'views',
    'static_path': 'statics'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler),
    (r"/login", LoginHandler),
    (r"/check_code", CheckCodeHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()


# 登录测试session：http://127.0.0.1:8000/index?u=whisky
# 登录测试验证码：http://127.0.0.1:8000/login


