#!/usr/bin/env python
# -*-coding:utf-8 -*-
from wsgiref.simple_server import make_server


def new():
    return 'new'


def index():
    return 'index'


URLS = {
    '/new': new,
    '/index': index,
}


def RunServer(environ, start_response):

    """
    :param environ:  封装了所有的请求信息
    :param start_response:
    :return:
    """

    start_response('200 OK', [('Content-Type', 'text/html')])

    url = environ['PATH_INFO']
    if url in URLS.keys():
        func_name = URLS[url]
        ret = func_name()
    else:
        ret = '404'
    return ret


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    httpd.serve_forever()

