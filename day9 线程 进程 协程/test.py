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





"""

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

"""




# 协程（也叫微线程）：【工作的最小单位仍然是线程，协程本质是控制线程的执行】
# 相当于把线程分块，避免线程等待，应用场景举例：爬虫应用中，有5个线程爬取一个网站上的5个图片，当5个线程发出5个HTTP请求之后，都在等待回应，造成资源浪费；用协程只需1个线程，发出一个请求后，再去依次请求另4个网站，谁有应答再去接收应答进行IO操作。

from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()                # 表示切换到test2函数执行
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()                # 调回test1函数，并从上次的位置继续执行
    print(78)


gr1 = greenlet(test1)   # 创建一个协程
gr2 = greenlet(test2)

gr1.switch()    # 主线程执行到此，执行test1函数


# 结果：
12
56
34
78