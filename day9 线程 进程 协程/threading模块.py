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



# multiprocessing模块, python多进程实现，用发放类似多线程模块
# multiprocessing是python的多进程管理包，和threading.Thread类似。直接从侧面用subprocesses替换线程使用GIL的方式，由于这一点，multiprocessing模块可以让程序员在给定的机器上充分的利用CPU。
# 在multiprocessing中，通过创建Process对象生成进程，然后调用它的start()方法，注意：由于进程之间的数据需要各自持有一份，所以创建进程需要的非常大的开销。

from multiprocessing import Process


def f(name):
    print('hello', name)


if __name__ == '__main__':              # 使用进程模块最好加上这句，否则有时候会报错
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
"""
"""
进程的daemon方法：
# 代码从上到下解释，由主线程负责，主线程保存在主进程中；主线程又创建了两个子进程，两个子进程中的线程执行的print（a1）
import multiprocessing
import time


def f1(a1):
    time.sleep(2)
    print(a1)

if __name__ == '__main__':
    for i in range(10):
        t = multiprocessing.Process(target=f1, args=(i,))
        # t.daemon = True             # 类似于线程中的setDaemon方法： 主进程执行完毕后是否等待子进程执行
        t.start()
        t1 = multiprocessing.Process(target=f1, args=(i,))
        # t1.daemon = True
        t1.start()
        print('end')                  # 结果中先输出end，可知主线程一次执行完代码



# 进程的join方法
import multiprocessing
import time


def f1(a1):
    time.sleep(2)
    print(a1)

if __name__ == '__main__':
    t = multiprocessing.Process(target=f1, args=(1,))
    t.start()
    print('111')
    t.join()             # 进程的阻塞，先输出111，等t进程执行结束，继续向下执行，join（2）最多等两秒
    print('222')
    t1 = multiprocessing.Process(target=f1, args=(2,))
    t1.start()

# 方法一，Array
from multiprocessing import Process, Array


def Foo(i, temp):
    temp[i] = 100 + i
    for item in temp:
        print(i, '----->', item)

if __name__ == '__main__':
    temp = Array('i', [11, 22, 33, 44])
    for i in range(2):
        p = Process(target=Foo, args=(i, temp, ))
        p.start()

#方法二：manage.dict()共享数据，字典中没有元素个数限制，也没有类型限制

from multiprocessing import Process, Manager
import time

def Foo(i, dic):
    dic[i] = 100 + i
    #print(dic.values())
    print(len(dic))

if __name__ == '__main__':
    manage = Manager()
    dic = manage.dict()       # 特殊方法创建的字典，进程之间可以共享数据
    # dic = {}               # 普通字典，进程之间无法共享数据
    for i in range(2):
        p = Process(target=Foo, args=(i, dic, ))
        p.start()
        #p.join()
    time.sleep(5)
"""

# 进程池
# 用Pool类创建一个进程池， 展开提交的任务给进程池
"""
from multiprocessing import Pool
import time


def myFun(i):
    time.sleep(2)
    return i+100


def end_call(arg):
    print("end_call", arg)


# print(p.map(myFun,range(10)))
if __name__ == '__main__':      # 如果不写此句，windows下不支持进程的创建,临时模拟用，如果需要运行多进程，应在linux下运行
    p = Pool(5)                 # 创建5个进程
    for i in range(10):
        p.apply_async(func=myFun, args=(i,), callback=end_call)  # callback是回调函数，func中的任务执行完后，会调用callback

    print("end")
    p.close()
    p.join()



from multiprocessing import Pool
import time


def Foo(i):
    time.sleep(2)
    return i + 100


def Bar(arg):
    print(arg)

pool = Pool(5)  # 最多创建5个进程
# print pool.apply(Foo,(1,))                            # 生成一个进程去执行Foo
# print pool.apply_async(func = Foo, args=(1,)).get()    # 执行完后Foo后执行另外一个函数表示执行完了

for i in range(10):
    pool.apply_async(func=Foo, args=(i,), callback=Bar)  # 回调函数callback：执行完Foo函数，自动去调用Bar方法，并且将Foo函数的返回值赋值给bar方法

print('end')
pool.close()
pool.join()  # 进程池的join方法，进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。

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

# pool.apply        每个进程之间是串行执行的，每一个任务排队进行;每个进程都有一个join方法
# pool.apply_async  进程之间并发执行，没有join方法，且进程的daemon=rue；另外可以设置回调函数：callback，回调函数的参数是f1函数中的返回值
# pool.join()       进程池的join方法（等所有的子进程执行完，主进程终止），必须先执行close方法。（查看源码可知，如果没有执行进程池的close或terminate方法，会报错）
# pool.close()      for循环中的任务执行完后，关闭进程池，终止主进程
# pool.terminate()  立即终止所有for循环中的任务。

"""




# 自定义线程池：
# 1. 队列中放任务，线程去队列中取任务,重复利用同一个线程执行多个任务

import queue
import threading
import contextlib
import time


StopEvent = object()   # StopEvent = 10  写成什么都可以


class ThreadPool(object):

    def __init__(self, max_num):
        """
        :param max_num:  最多创建的线程数（线程池最大容量）
        """
        self.q = queue.Queue()          # 队列长度无限制
        self.max_num = max_num          # 最多创建的线程数（线程池最大容量）

        self.generate_list = []         # 真实创建的线程数，放入列表（并发量很大，任务很耗时，线程数才会开满）
        self.free_list = []             # 空闲线程数量，空闲线程（已经创建好的）大于0，则不用创建新的线程
        self.terminal = False

    def run(self, func, args, callback=None):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行成功或失败后执行的回调函数
        :return: 如果线程池已经终止，则返回True否则None
        """
        w = (func, args, callback, )    # 封装任务信息到元组中
        self.q.put(w)                   # 把任务放入队列中

        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:  # 空闲线程为0且不超过最大线程数就会创建线程，有空闲线程不创建新的线程
            self.generate_thread()

    def generate_thread(self):
        """
        创建线程
        :return:
        """
        t = threading.Thread(target=self.call)
        t.start()

    @contextlib.contextmanager
    def work_state(self, state_list, worker_thread):
        """
        用于记录线程中正在等待的线程数，即空闲的线程数
        :param state_list:         空闲列表
        :param worker_thread:
        :return:
        """
        state_list.append(worker_thread)
        try:
            yield
        finally:
            state_list.remove(worker_thread)

    def call(self):
        """
        循环去获取任务函数并执行任务函数，每创建一个线程都会执行call方法
        :return:
        """
        current_thread = threading.currentThread()     # Return the current Thread object 获取当前线程对象
        self.generate_list.append(current_thread)

        # 取任务并执行
        event = self.q.get()                            # 取队列中的任务元组
        while event != StopEvent:

            func, args, callback = event                 # 开始执行任务
            try:                                         # 执行任务可能失败
                result = func(*args)
                status = True
            except Exception as e:
                status = False
                result = e

            if callback is not None:                    # 回调函数存在
                try:
                    callback(status, result)              # 返回值传给回调函数
                except Exception as e:
                    pass

            if self.terminal:
                event = StopEvent
            else:
                with self.work_state(self.free_list, current_thread):         # 利用上下文管理优化代码
                    event = self.q.get()
                    # self.free_list.append(current_thread)        # 执行任务后线程空闲
                    # event = self.q.get()                         # 去队列中取新的任务
                    # self.free_list.remove(current_thread)        # 取到任务，移除当前线程
        else:
            # event不是元组，不是任务, 线程池中任务取光了，接收到了停止符（StopEvent）
            self.generate_list.remove(current_thread)


    def close(self):
        """
        generate_thread 创建了多少线程，就添加多少个停止标记（StopEvent）,当遇到停止标记，退出call方法的while循环，线程停止，等待回收
        :return:
        """
        num = len(self.generate_list)
        while num:
            self.q.put(StopEvent)
            num -= 1

    def terminate(self):
        """
        立即结束执行任务的线程,清空任务队列
        :return:
        """
        self.terminal = True
        while self.generate_list:
            self.q.put(StopEvent)
        self.q.empty()

    def action(self):
        pass


def work(i):
    time.sleep(0.5)
    print(i)

pool = ThreadPool(5)
for itme in range(20):
    pool.run(func=work, args=(itme,))

time.sleep(2)
pool.terminate()

#time.sleep(3)           # 阻塞主线程 查看实验结果
#print(len(pool.generate_list))   # 当任务耗时很小时，只需很少的线程即可完成任务，当任务耗时0.5秒free_list为0，不断创建新的线程





"""

"""
