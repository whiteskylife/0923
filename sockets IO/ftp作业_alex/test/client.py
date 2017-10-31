# -*- coding: utf-8 -*-

import socket

obj = socket.socket()
ip = ('127.0.0.1', 9999)
obj.connect(ip)

while True:
    str_content = str(obj.recv(1024), encoding='utf-8')
    print(str_content)
    inputs = input('>>> ')
    obj.sendall(bytes(inputs, encoding='utf-8'))