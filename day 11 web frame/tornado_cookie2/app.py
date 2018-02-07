#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web

container = {}
# container = {
#     '第一个人的随机字符串': {},
#     '第二个人的随机字符串': {'k1': 111, 'parents': '你'},
# }


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument('u', None) in ['whisky', 'alex']:     # 设置u值默认为None，否则访问不带u参数会报400错误
            import hashlib
            import time
            obj = hashlib.md5()
            obj.update(bytes(str(time.time()), encoding='utf-8'))
            random_str = obj.hexdigest()
            container[random_str] = {}

            container[random_str]['k1'] = 123
            container[random_str]['k2'] = self.get_argument('u', None) + 'parents'
            container[random_str]['is_login'] = True
            self.set_cookie('iiiiiiii', random_str)
            self.write('服务器端设置cookie完成')

        else:
            self.write('请用正确的用户名登录')


class ManagerHandler(tornado.web.RequestHandler):
    def get(self):
        random_str = self.get_cookie('iiiiiiii')
        current_user_info = container.get(random_str, None)
        if not current_user_info:       # 如果大字典中用户信息为空（random_str键的值为none）
            self.redirect('/index')
        else:
            # current_user_info有值时，还有两种情况：1.存在is_login，且值为true；2.存在is_login，且值为false（服务器端主动设置session过期）
            if current_user_info.get('is_login', None):  # 存在is_login，且值为true；
                temp = " %s - %s" % (current_user_info.get('k1', ''), current_user_info.get('k2', ''))   # 没有默认为空，字符串格式化中用none会报错
                self.write(temp)
            else:
                self.redirect('/index')



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


