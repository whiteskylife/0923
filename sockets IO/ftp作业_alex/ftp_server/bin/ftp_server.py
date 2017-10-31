#!/usr/bin/env python
# -*- coding utf-8 -*-

import os
import sys
import socketserver

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))  #和下面方式的区别在于路径的斜杠
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

if __name__ == '__main__':
    main.ArgvHandler()


class FtpServer(socketserver.BaseRequestHandler):
    def handler(self):
        print('---------------------------------')
        pass
