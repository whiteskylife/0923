#!/usr/bin/env python
# -*- coding utf-8 -*-

import threading
import queue
"""
message = queue.Queue(10)  # 生成队列


def producer(i):
    message.put(i)   # put是阻塞的
    print('put----------', i)


def consumer(i):
    nsg = message.get()
    print('get----------', i)


for i in range(12):
    t = threading.Thread(target=producer, args=(i,))
    t.start()

for i in range(10):
    t = threading.Thread(target=consumer, args=(i,))
    t.start()


q = queue.Queue(maxsize=0)  # 构造一个先进先出队列，maxsize指定队列长度，为0 时，表示队列长度无限制。

常用下面四个：
q.put(item, block=True, timeout=None) # 将item放入Queue尾部，item必须存在，可以参数block默认为True,表示当队列满时，会等待队列给出可用位置，为False时为非阻塞，此时如果队列已满，会引发queue.Full 异常。 可选参数timeout，表示 会阻塞设置的时间，过后，如果队列无法给出放入item的位置，则引发 queue.Full 异常
q.get(block=True, timeout=None)      # 移除并返回队列头部的一个值，可选参数block默认为True，表示获取值的时候，如果队列为空，则阻塞，为False时，不阻塞，若此时队列为空，则引发 queue.Empty异常。 可选参数timeout，表示会阻塞设置的时候，过后，如果队列为空，则引发Empty异常。
q.put_nowait(item)              # 等效于 put(item,block=False)
q.get_nowait()                  # 等效于 get(item,block=False)


q.join()    # 等到队列为kong的时候，在执行别的操作
q.qsize()   # 返回队列的大小 （不可靠）
q.empty()   # 当队列为空的时候，返回True 否则返回False （不可靠）
q.full()    # 当队列满的时候，返回True，否则返回False （不可靠）

"""

from multiprocessing import Process


def f(name):
    print('hello', name)


if __name__ == '__main__':              # 使用进程模块最好加上这句，否则有时候会报错
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()