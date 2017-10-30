#!/usr/bin/env python
# -*- coding utf-8 -*-

import optparse


class ArgvHandler(object):
    def __init__(self):
        self.parser = optparse.OptionParser()
        # parser.add_option('-s', '--host', dest='host', help='server binding host address')
        # parser.add_option('-p', '--port', dest='port', help='server binding port')
        (options, args) = self.parser.parse_args()   # 解析输入的参数是否符合规则，把结果返回（options：add_options中输入的参数，args，不在add_option中的参数）
        self.verify_args(options, args)

    def verify_args(self, options, args):
        """
        校验并调用相应的功能
        :param options: optparse模块分析参数，add_options中输入的参数
        :param args:    列表形式，传入且不在add_option中的参数
        :return:
        """
        if hasattr(self, args[0]):
            func = getattr(self, args[0])
            func()
        else:
            self.parser.print_help()

    def start(self):
        print('start server...'.center(50, '-'))
