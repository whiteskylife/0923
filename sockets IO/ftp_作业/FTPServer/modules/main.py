#!/usr/bin/env python
# -*- coding utf-8 -*-
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings
import socketserver
from modules import threading_socket_server


class ArgvHandler:
    """
    参数处理
    """
    def __init__(self, args):
        self.args = args        # 接收参数列表
        self.argv_parse()       # 解析参数

    def argv_parse(self):
        """
        传入参数分析
        :return:
        """
        if len(self.args) < 1:
            self.help_msg()
        else:
            first_argv = self.args[1]
            if hasattr(self, first_argv):
                func = getattr(self, first_argv)
                func()                              # 执行start方法
            else:
                self.help_msg()

    def start(self):
        """
        启动socketserver
        :return:
        """
        try:
            print('FTPserver starting...'.center(50, '-'))
            server = socketserver.ThreadingTCPServer((settings.BIND_HOST, settings.BIND_PORT),
                                                     threading_socket_server.MyTCPHandler)
            print('server started...')
            server.serve_forever()
        except KeyboardInterrupt:
            pass



    def help_msg(self):
        msg = '''
            start
            stop
            '''
        print(msg)
