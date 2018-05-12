#!/usr/bin/env python
# -*-coding:utf-8 -*-


from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

import socket
import json

'''
obj = socket.socket()

url1 = (('www.gxyclub.com', 443))
url = '/'
host = 'www.gxyclub.com'
obj.connect(url1)
inp = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (url, host)


obj.sendall(bytes(inp, encoding='utf-8'))
a = obj.recv(1024)
b = a.decode('utf-8')
print(type(b), b)
# print(a)
# print(type(a))
# ret = json.loads(str(a, encoding='utf-8'))
# print(ret)
# print(type(ret))
'''

'''
# 阻塞
client = socket.socket()
client.connect(('113.107.45.172', 80))  # 阻塞
# client.connect(('180.97.162.175', 80))  # 阻塞

data = b"GET / HTTP/1.1\r\nHost: dig.chouti.com\r\n\r\n"
client.sendall(data)

response = client.recv(8096)
print(response)


client.close()
# 非阻塞
client = socket.socket()
client.setblocking(False)
client.connect(('113.107.45.172', 80))  # 阻塞
# client.connect(('180.97.162.175', 80))  # 阻塞

# 发送请求
data = b"GET / HTTP/1.1\r\nHost: dig.chouti.com\r\n\r\n"
client.sendall(data)

response = client.recv(8096)
print(response)


client.close()
'''

import select
select.select()