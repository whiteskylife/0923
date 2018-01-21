#!/usr/bin/env python
# -*-coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
from jinja2 import Template

def new():
    # html_file = open(os.path.join('views', "html basic.html"), 'r')
    # data = html_file.read()
    # html_file.close()
    # data = data.replace("{{item}}", str(time.time()))
    # return data

    f = open(os.path.join('views', 'html basic.html'))
    result = f.read()

    template = Template(result)
    data = template.render(name='John Doe', user_list=['alex', 'eric','xiaojun', 'sb', 'alex', '222'])
    return data.encode('utf-8')

def index():
    return 'index'


def home():
    return 'home'