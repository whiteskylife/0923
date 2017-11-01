# -*- coding: utf-8 -*-

import socketserver
'''
socket只能同时处理一个请求
import socket

obj = socket.socket()
ip_port = ('127.0.0.1', 9999)
obj.bind(ip_port)
obj.listen(5)

while True:
    conn, ip = obj.accept()
    while True:
        ret = str(conn.recv(1024), encoding='utf-8')
        if ret == 'q':
            break
        conn.sendall(bytes(ret + 'server reply...', encoding='utf-8'))

'''


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):        # 必须叫这个方法名称，ThreadingTCPServer内写死了要调这个方法
        # self 封装了属性如下，可以生成多个服务端响应请求
        # self.request(客户端请求), self.client_address（客户端地址）,self.servers（服务器对象）
        conn = self.request
        conn.sendall(bytes('welcome login whiskys python world', encoding='utf-8'))
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes, encoding='utf-8')
            if ret_str == 'q':
                break
            conn.sendall(bytes(ret_str + 'OK', encoding='utf-8'))

if __name__ == '__main__':
    """
    server对象封装了：
            self.server_address ==> ('127.0.0.1', 9999)
            self.RequestHandlerClass ==> MyServer
            self.socket             ==>  创建服务器端的socket对象
    """
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()



