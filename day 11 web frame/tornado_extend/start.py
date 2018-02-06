#!/usr/bin/env python
# -*-coding utf-8 -*-

import tornado.web
from views import extend

settings = {
    'template_path': 'views',
}

application = tornado.web.Application([
    (r"/index", extend.IndexHandler),
    (r"/fuckoff", extend.FuckoffHandler),

], **settings)