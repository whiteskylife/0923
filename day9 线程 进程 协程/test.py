#!/usr/bin/env python
# -*- coding utf-8 -*-

# !/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Pool
import time


# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield
#         #print(b)
#         a, b = b, a + b
#         n = n + 1
#
#
# #fab(5)
#
# for i in fab(5):
#     print(i)
#
#


# def xrange():
#     print('start')
#     start = 0
#     while True:
#         yield
#         start += 1
#
# obj = xrange()
# r = obj.__next__()
# r = obj.__next__()
# r = obj.__next__()
# print(r)
#


# def worker_state(xxx, val):
#     xxx.append(val)
#     try:
#         yield
#     finally:
#         xxx.remove(val)
#
# q = queue.Queue()
# li = []
# # li.append(1)
# # q.get()
# # li.remove(1)
#
# with worker_state(li, 1):           # 作用相当于上面注释的三行代码
#     #print('before', li)
#     q.get()







# 上下文管理

# 自定义open，with open打开文件原理
import contextlib


@contextlib.contextmanager
def myopen(file_path, mode):
    f = open(file_path, mode, encoding='utf-8')
    try:
        yield f
    finally:
        f.close()


with myopen('index.html', 'r') as file_obj:
    print(file_obj.readline())

# yield f会把f返回给file_obj，