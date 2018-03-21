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
setDaemon设置为false（默认）时，在主程序退出之前需要告诉线程在什么时候退出，主程序会等待子线程执行完再退出；
setDaemon设置为True时，当主程序退出时，线程自动被结束（killed）
'''


import time
import threading


def run(n):
    print('[%s]------child thread running----\n' % n)
    time.sleep(2)
    print('--child thread done--')


def main():
    for i in range(5):
        t = threading.Thread(target=run, args=[i, ])
        t.start()
        t.join(1)
        print('starting child thread', t.getName())


m = threading.Thread(target=main, args=[])
print('starting Main thread %s' % m.getName())
# m.setDaemon(True)  # 将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
m.start()
m.join(timeout=3)
# m.join()
print("---main thread done----")


# Note：Daemon threads are abruptly stopped at shutdown. Their resources (such as open files, database transactions, etc.) may not be released properly.
# If you want your threads to stop gracefully, make them non-daemonic and use a suitable signalling mechanism such as an Event.