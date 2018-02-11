#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web

IMG_LIST = []


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', img_list=IMG_LIST)

    def post(self, *args, **kwargs):
        print(self.get_argument('user'))
        # checkbox 要用get_arguments来获取
        print(self.get_arguments('favor'))
        # print(self.get_arguments('fafafa'))
        # tornado内部是通过yeild来做的self.request.files，所以不支持索引方式，必须用循环方式去取
        file_metas = self.request.files['file_upload']      # 前台name变量传过来的文件名
        for meta in file_metas:
            # 要上传的文件名
            file_name = meta['filename']
            import os
            with open(os.path.join('statics', 'img', file_name), 'wb') as up:
                up.write(meta['body'])
                IMG_LIST.append(file_name)
        self.write('文件上传完成')


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
