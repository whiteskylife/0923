#!/usr/bin/env python
# -*-coding:utf-8 -*-
import socket
import select
select.select()

class AsynchronousNonBlocking(object):
    def __init__(self):
        self.sock_list = []
        self.conns = []

    def add_request(self, req_info):
        """
        创建请求
         req_info: {'host': 'www.baidu.com', 'port': 80, 'path': '/'},
        :return:
        """
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect((req_info['host'], req_info['port']))
        except BlockingIOError as e:
            pass

        # obj = Request(sock, req_info)
        self.sock_list.append(obj)
        self.conns.append(obj)


    def run(self):
        """开始事件循环"""
        pass


url_list = [
    {'host': 'www.baidu.com', 'port': 80, 'path': '/'},
    {'host': 'www.cnblogs.com', 'port': 80, 'path': '/'},
    {'host': 'www.bing.com', 'port': 80, 'path': '/'},
]

obj = AsynchronousNonBlocking()
for item in url_list:
    obj.add_request(item)
