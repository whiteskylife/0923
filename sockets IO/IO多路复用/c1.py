# -*- coding: utf-8 -*-

import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))
recv_content = str(obj.recv(1024), encoding='utf-8')
print(recv_content)

obj.close()
