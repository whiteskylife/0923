# -*- coding: utf-8 -*-

# 基于socketserver实现的FTP

import hashlib
import socket
import socketserver


class MyServer(socketserver.BaseRequestHandler):
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
    内部原理：socket + select + 多线程   ===》 实现处理并发操作

    handle：负责处理

    server_address = ('127.0.0.1', 9999)
    MyServer ==> RequestHandlerClass

    ThreadingTCPServer负责：
    1. ThreadingMixIn:  创建多线程
    2. TCPServer：      初始化:服务器IP，端口。  绑定IP、端口，并监听
    3. BaseServer:      self.server_address = server_address      self.RequestHandlerClass = RequestHandlerClass
    4. serve_forever:   通过select.select实现的IO多路复用

    server 对象中封装了：
        self.server_address ('127.0.0.1', 9999)
        self.RequestHandlerClass  MyServer
        self.socket

    '''

    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()


