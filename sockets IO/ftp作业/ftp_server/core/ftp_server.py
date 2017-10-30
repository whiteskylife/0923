# -*- coding: utf-8 -*-

import socketserver


class FtpServer(socketserver.BaseRequestHandler):
    def handler(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
        pass

if __name__ == '__main__':
    HOST, PORT = 'localhost', 9000

