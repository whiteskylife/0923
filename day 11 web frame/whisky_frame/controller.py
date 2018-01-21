#!/usr/bin/env python
# -*-coding:utf-8 -*-
import os


def new():
    html_file = open(os.path.join('views', "html basic.html"), 'r')
    data = html_file.read()
    html_file.close()
    return data
    # return '<html><head><body><h1 style="color:red;">asdf</h1></body></head></html>'


def index():
    return 'index'


def home():
    return 'home'