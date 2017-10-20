# -*- coding: utf-8 -*-

import socket

obj = socket.socket()
ip = ('127.0.0.1', 8002)
obj.connect(ip)
obj.close()