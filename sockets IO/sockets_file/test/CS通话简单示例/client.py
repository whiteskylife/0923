# -*- coding: utf-8 -*-

# CS通话简单示例

import socket

obj = socket.socket()
ip_port = ('127.0.0.1', 8000)
obj.connect(ip_port)

ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes, encoding='utf-8')
print(ret_str)
while True:
    data = input('>')
    obj.send(bytes(data,encoding='utf-8'))
