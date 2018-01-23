#!/usr/bin/env python
# -*-coding:utf-8 -*-

import tornado.ioloop
import tornado.web
INPUTS_LIST = []


# 处理请求的类:
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render('s1.html', xxxooo=INPUTS_LIST)

    def post(self, *args, **kwargs):
        name = self.get_argument('xxx')     # 获取用户提交的数据
        INPUTS_LIST.append(name)
        self.render("s1.html", xxxooo=INPUTS_LIST)


# 对于静态文件的处理
settings = {
    "template_path": "tpl",        # 模板路径配置
    'static_path': 'static',       # 静态文件指定路径
    # "static_url_prefix": '/prefix_folder/'  # 如果写上了static_url_prefix , 会去static_path路径中去找对应的路径，
}

# 路由映射，路由系统
application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)

# 下面做了两件事：1.创建socket对象；2.循环socket对象。内部用了epoll，select，IO多路复用
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
