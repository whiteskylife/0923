# -*- coding: utf-8 -*-

# 基于socketserver实现的FTP

import hashlib
import socket
import socketserver




class MyServer(socketserver.BaseRequestHandler):
    '''
    '''
    def handle(self):
        conn = self.request
        conn.sendall(bytes('欢迎登录FTP服务器---', encoding='utf-8'))

        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes, encoding='utf-8')
            if ret_str == 'q':
                break
            conn.sendall(bytes(ret_str + 'OK', encoding='utf-8'))



if __name__ == '__main__':
    '''
    server_address = ('127.0.0.1', 9999)
    RequestHandlerClass = MyServer

    ThreadingTCPServer负责：
    1. ThreadingMixIn:  创建进程
    2. TCPServer：      初始化:服务器IP，端口。  绑定IP、端口，并监听
    3. BaseServer:      self.server_address = server_address      self.RequestHandlerClass = RequestHandlerClass
    4. serve_forever:   通过select.select实现的IO多路复用
    '''

    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()


def login():
