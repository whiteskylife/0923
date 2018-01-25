#!/usr/bin/env python
# -*-coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import uimethod as mt       # 导入
import uimodule as md

INPUTS_LIST = []


# 处理请求的类:
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         # self.write("Hello, world")
#         name = self.get_argument('xxx', None)     # 获取用户提交的数据
#         if name:
#             INPUTS_LIST.append(name)
#         self.render('s1.html', npm="NPM_test", xxxooo=INPUTS_LIST)

    # def post(self, *args, **kwargs):
    #     name = self.get_argument('xxx')     # 获取用户提交的数据
    #     INPUTS_LIST.append(name)
    #     self.render("s1.html", xxxooo=INPUTS_LIST)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('chouti.html')

settings = {
    "template_path": "tpl",        # 模板路径配置(存放HTML)
    'static_path': 'static',       # 静态文件指定路径（存放JS、CSS）
    # "static_url_prefix": '/prefix_folder/'  # 如果写上了static_url_prefix , 会去static_path路径中去找对应的路径，
    'ui_methods': mt,               # 注册
    'ui_modules': md,               # 注册
}

# 路由映射，路由系统
application = tornado.web.Application([
    # (r"/index", MainHandler),
    (r"/index", IndexHandler),
], **settings)

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
