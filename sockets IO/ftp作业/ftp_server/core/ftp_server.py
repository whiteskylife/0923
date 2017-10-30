# -*- coding: utf-8 -*-

import socketserver

class FtpServer(socketserver.BaseRequestHandler):
    def handler(self):
        print('---------------------------------')
        pass

if __name__ == '__main__':
    HOST, PORT = 'localhost', 9000

