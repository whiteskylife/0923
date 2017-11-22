#!/usr/bin/env python
# -*- coding utf-8 -*-

# !/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Pool
import time


def f1(a):
    time.sleep(1)
    print(a)
    return 1000


def f2(arg):
    print(arg)


if __name__ == '__main__':
    pool = Pool(5)
    for i in range(5):
        #pool.apply(func=f1, args=(i,))       # apply申请进程池中的进程的时候是一个一个去申请并执行，执行后才申请下一个, 相当于加了一个join方法
        pool.apply_async(func=f1, args=(i,), callback=f2)   # 异步申请进程，主进程没有等待子进程执行完再退出
        print('111111111111111111')
    pool.close()  # for循环中的任务执行完后，关闭进程池，终止主进程
    # pool.terminate()  # 立即终止所有for循环中的任务。
    pool.join()         # 进程池的join方法（等所有的子进程执行完，主进程终止），必须先执行close方法。（查看源码可知，如果没有执行进程池的close或terminate方法，会报错）