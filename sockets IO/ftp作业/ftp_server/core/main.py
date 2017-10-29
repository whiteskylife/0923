#!/usr/bin/env python
# -*- coding utf-8 -*-

import optparse


class ArgvHandler(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option('-s', '--host', dest='host', help='server binding host address')
        parser.add_option('-p', '--port', dest='port', help='server binding port')
        (options, args) = parser.parse_args()   # 解析输入的参数是否符合规则，把结果返回（options：add_options中输入的参数，args，不在add_option中的参数）
        print('parser', options, args)
        print(options.host, options.port)
