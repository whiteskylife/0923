#!/usr/bin/env python
# -*-coding:utf-8 -*-

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

'''

import threading
import queue

message = queue.Queue(10)  # 生成队列


def producer(i):
    message.put(i)   # put是阻塞的
    print('put----------', i)


def consumer(i):
    nsg = message.get()
    print('get----------', i)
    print('get--- %s' % nsg)


for i in range(12):
    t = threading.Thread(target=producer, args=(i,))
    t.start()

for i in range(10):
    t = threading.Thread(target=consumer, args=(i,))
    t.start()