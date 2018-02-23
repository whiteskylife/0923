#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        callback = self.get_argument('callback')
        self.write('%s([11,22,33]);' % callback)

    def post(self, *args, **kwargs):
        self.write('t2.post')


class CorsHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('{"status":1, "message": "get"}')

    def post(self, *args, **kwargs):
        # set_header设置响应头和它的值(客户端的值)，表示允许这个域名来我这发跨域的ajax请求,携带我这里服务器端的响应头回去，浏览器不再阻止
        # 多个域名后面逐一加上逗号分隔，让所有客户端都能访问域名的值设置为“*”：self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Origin', 'http://whisky.com:8001')
        self.write('{"status":1, "message": "post"}')

    def options(self, *args, **kwargs):
        # 对于复杂请求，预检的时候默认先执行这个potions方法
        print('options')
        self.set_header('Access-Control-Allow-Origin', '*')     # 允许客户端网站来请求
        self.set_header('Access-Control-Allow-Methods', "PUT, DELETE")  # 允许PUT方法
        self.set_header('Access-Control-Allow-Headers', "h1,h2")     # 允许请求头的key
        # self.set_header('Access-Control-Max-Age', 10)     # 设置超时时间，10s内只需通过一次预检，10s后再次预检

    def put(self, *args, **kwargs):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.write('ok')


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/cors", CorsHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8002)
    tornado.ioloop.IOLoop.instance().start()
