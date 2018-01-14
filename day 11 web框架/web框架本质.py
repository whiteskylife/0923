#!/usr/bin/env python
# -*- coding: utf-8-*-
#-*-coding:utf-8 -*-
from wsgiref.simple_server import make_server


def RunServer(environ, start_response):
    '''

    :param environ: 封装了所有的请求信息
    :param start_response:
    :return:
    '''
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    httpd.serve_forever()