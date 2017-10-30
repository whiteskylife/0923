#!/usr/bin/env python
# -*- coding utf-8 -*-

import os
import json
import optparse
import socket


class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option('-s', '--server', dest='server', help='ftp server ip addr')
        parser.add_option('-P', '--port', type='int', dest='port', help='ftp server port')
        parser.add_option('-u', '--username', dest='username', help='username')
        parser.add_option('-p', '--password', dest='password', help='password')
        self.options, self.args = parser.parse_args()
        self.verify_args(self.options, self.args)

    def make_connection(self):
        """
        客户端连接服务器端
        :return:
        """
        self.sock = socket.socket()
        self.sock.connect((self.options.server, self.options.port))

    def verify_args(self, options, args):
        """
        校验参数合法性
        :param options:
        :param args:
        :return:
        """

        if options.username is not None and options.password is not None:
            pass
        else:
            if options.username is None or options.password is None:
                print('Err: username or password must be provided together')

        if options.server and options.port:
            print(options)
            if options.port >0 and options.port <65535:
                return True
            else:
                exit('Err: host port must in 0-65535')

    def authenticate(self):
        """
        用户身份验证
        :return:
        """
        if self.options.username:
            print(self.options.username, self.options.password)
            self.get_auth_result(self.options.username, self.options.password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input('username: ').strip()
                password = input('password: ').strip()
                self.get_auth_result(username, password)

    def get_auth_result(self, user, password):
        data = {'action': 'auth',
                'username': user,
                'password': password,
                }
        self.sock.send(json.dumps(data).encode())
        self.get_response()
    def get_response(self):
        """
        得到服务器端回复结果
        :return:
        """
        data = self.sock.recv(1024)
        data = json.loads(data)
        print('response: ', data)

    def interactive(self):
        if self.authenticate():
            print('')


if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive()  # 交互
