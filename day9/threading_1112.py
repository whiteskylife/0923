#!/usr/bin/env python
# -*- coding utf-8 -*-

import threading
import time

"""

创建线程目的：并发执行任务
setDaemon： 主线程执行完毕后是否等待子线程执行
默认False：代码中主线程执行完，等待子线程执行完毕，退出程序；设置为True：代码中的主线程执行完，子线程停止执行

import threading
import time

def run(n):
    print('task ----------------', n)
    time.sleep(3)


t = threading.Thread(target=run, args=(1, ))
t.setDaemon(True)
t.start()
t1 = threading.Thread(target=run, args=(2, ))
t1.setDaemon(True)
t1.start()
t2 = threading.Thread(target=run, args=(3, ))
t2.setDaemon(True)
t2.start()
# 上面的代码执行时，同时输出函数中的print内容



join[n]：  逐个执行每个线程，执行完毕后继续往下执行，该方法使得多线程变得无意义, 可选参数n，最多等待n秒，不加参数一直等待子线程执行完再向下执行

import threading
import time

def run(n):
    print('task ----------------', n)
    time.sleep(10)


t = threading.Thread(target=run, args=(1, ))
t.start()
t.join(1)
t1 = threading.Thread(target=run, args=(2, ))
t1.start()
t2 = threading.Thread(target=run, args=(3, ))
t2.start()

# 线程锁

count = 0
lock = threading.RLock()  # 创建锁


def func():
    lock.acquire()  # 获得锁
    global count
    count += 1
    time.sleep(1)
    print(count)
    lock.release()  # 释放锁


for i in range(10):
    t = threading.Thread(target=func)
    t.start()

# 运行代码可知：程序需等待前一个线程把这个操作执行完，把锁释放release，才能操作全局变量
"""


# threading.Event : 线程间通信的机制之一，一个线程发送一个event信号，其他的线程则等待这个信号。用于主线程控制其他线程的执行，事件主要提供了三个方法 set、wait、clear

import threading


def do(event):
    print('start')
    event.wait()  # Event.wait([timeout]) ： 作用：堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）
    print('execute')


event_obj = threading.Event()
for i in range(10):
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()

event_obj.clear()       # 将标识位设为False（默认）
inp = input('input:')
if inp == 'true':
    event_obj.set()     # 将标识位设为True
