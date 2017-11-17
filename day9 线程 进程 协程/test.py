#!/usr/bin/env python
# -*- coding utf-8 -*-

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
    for i in range(40):
        # pool.apply(func=f1, args=(i,))       # apply申请进程池中的进程的时候是一个一个去申请并执行，执行后才申请下一个, 相当于加了一个join方法
        pool.apply_async(func=f1, args=(i,), callback=f2)   # 异步申请进程，主进程没有等待子进程执行完再退出
        print('111111111111111111')
    pool.close()
    pool.join()

# pool.apply        每个进程之间是串行执行的，每一个任务排队进行
# pool.apply_async  进程之间并发执行，另外可以设置回调函数：callback，回调函数的参数是f1函数中的返回值


