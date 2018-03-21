#!/usr/bin/env python
# -*- coding utf-8 -*-


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




'''


# 协程（也叫微线程）作用：协调线程【工作的最小单位仍然是线程，协程本质是控制线程的执行】
# 相当于把线程分块，避免线程等待，应用场景举例：爬虫应用中，有5个线程爬取一个网站上的5个图片，当5个线程发出5个HTTP请求之后，都在等待回应，造成资源浪费；用协程只需1个线程，发出一个请求后，再去依次请求另4个网站，谁有应答再去接收应答进行IO操作。

# 线程和进程的操作是由程序触发系统接口，最后的执行者是系统；协程的操作则是程序员。

# 协程存在的意义：对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时（保存状态，下次继续）。协程，则只使用一个线程，在一个线程中规定某个代码块执行顺序。

# 协程的适用场景：当程序中存在大量不需要CPU的操作时（IO），适用于协程；

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
# 小结：协程其实就是让一个线程执行多个任务，更节省资源、性能更高， greenlet只是了解协程概念，工程中不用，用另外一个模块gevent





gevent模块：

import gevent

# gevent内部调用的greenlet，自动调度，遇到IO请求自动切换执行下个请求任务， 下面的代码是手动切换线程意义不大
import gevent


def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])



# 遇到IO操作自动切换：

from gevent import monkey; monkey.patch_all()
import gevent
import requests

def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),         # 一个线程同时发了三个请求，比创建多线程更省资源
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
])

# 以后发送http请求，一个线程利用协程就搞定了，性能高， 爬虫模块scrapy内部就利用了gevent（遇到IO请求，自动切换下一个任务），gevent又调用了greenlet（调用协程），Python中涉及到高性能大多都和gevent有关系
import scrapy
'''


import threading
import time


def run(n):
    print('task ----------------', n)
    time.sleep(3)


# def run2(n):
#     print('task2-----------------', n)
#     time.sleep(3)


t = threading.Thread(target=run, args=(1, ))
t.setDaemon(True)
t.start()

t1 = threading.Thread(target=run, args=(2, ))
t1.setDaemon(True)
t1.start()


t2 = threading.Thread(target=run, args=(3, ))
t2.setDaemon(True)
t2.start()

# 上面的代码执行时，同时输出函数中的print内容,setDaemon为true时不会等待run方法中的3秒，主线程结束，直接退出程序
# Join & Daemon
# Some threads do background tasks, like sending keepalive packets, or performing periodic garbage collection, or whatever.
# These are only useful when the main program is running, and it's okay to kill them off once the other, non-daemon, threads have exited.

# Without daemon threads, you'd have to keep track of them, and tell them to exit, before your program can completely quit.
# By setting them as daemon threads, you can let them run and forget about them, and when your program quits, any daemon threads are killed automatically.