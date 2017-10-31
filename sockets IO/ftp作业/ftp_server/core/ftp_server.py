# -*- coding: utf-8 -*-

import socketserver
import json


class FtpServer(socketserver.BaseRequestHandler):
    def handler(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            data = json.loads(self.data.decode())
            if data.get('action') is not None:
                if hasattr(self, '__%s' % data.get('action')):
                    func = getattr(self, '__%s' % data.get('action'))
                    func(data)
                else:
                    print('invalid cmd')
            else:
                print('invalid cmd format')

    def __put(self, *args, **kwargs):
        """
        client send file to server
        :param args:
        :param kwargs:
        :return:
        """
    def __get(self, *args, **kwargs):
        pass

    def __ls(self, *args, **kwargs):
        pass

    def __cd(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    HOST, PORT = 'localhost', 9000

