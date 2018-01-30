#!/usr/bin/env python
# -*-coding:utf-8 -*-

import tornado.ioloop
import tornado.web


# render中的文件不要加/等路径

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        dic = {'status': True, "message": ""}
        user = self.get_argument('username')
        pwd = self.get_argument('password')
        # self.write('ok')    # write方法作用相当于console.log()
        if user == 'alex'and pwd == '123':
            pass
        else:
            dic['status'] = False
            dic['message'] = 'username or password is wrong!'
        import json
        self.write(json.dumps(dic))


settings = {
    "template_path": "views",  # 模板路径配置(存放HTML)
    # 'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh' # 加密cookie的盐
    "static_path": 'static',    # 注册引入jQuery的静态目录
}

# 路由映射，路由系统
application = tornado.web.Application([
    (r"/login", LoginHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
