#!/usr/bin/env python
# -*- coding utf-8 -*-

import os
import json
import optparse


class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option('-s', '--server', dest='server', help='ftp server ip addr')
        parser.add_option('-P', '--port', type='int', dest='port', help='ftp server port')
        parser.add_option('-u', '--username', dest='username', help='username')
        parser.add_option('-p', '--password', dest='password', help='password')
        self.options, self.args = parser.parse_args()
        self.verify_args(self.options, self.args)

    def verify_args(self, options, args):
        """
        校验参数合法性
        :param options:
        :param args:
        :return:
        """
        if options.server and options.port:
            print(options)
            if options.port >0 and options.port <65535:
                return True
            else:
                exit('Err: host port must in 0-65535')

    def interactive(self):
        pass

if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive()  # 交互
