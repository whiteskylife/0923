#!/usr/bin/env python
# -*-coding:utf-8 -*-
# tpl = "i am {0}, age {1}, really {0}".format("seven", 18)
# tpl = "i am {0[0]}, age {0[1]}, really {1[2]}".format([1, 2, 3], [11, 22, 33])
# print(tpl)
import twisted
from twisted.web.client import getPage, defer
from twisted.internet import reactor


def all_done(arg):     #这里的arg ，接收的是所有函数的返回值，
    print(arg)          # 打印结果[(回调函数是否抛出异常<True,False>,回调函数的返回值),(),()]
    reactor.stop()


def callback(contents):            # 回调函数
    print(contents)
    print(type(contents))
    # text = contents.decode('utf-8')
    # print(text)
    with open('a.html', mode='wb') as file:
        file.write(contents)



task = []

url_list = [
    # 'http://www.bing.com',
    # 'http://www.baidu.com',
    'http://dig.chouti.com',
]

for url in url_list:                                        # 循环过程中只是创建对象，加入列表，不会等待、阻塞
    obj = getPage(bytes(url, encoding='utf8'))                # getPage相当于requests,要传bytes类型的
    obj.addCallback(callback)                                # 对于每个请求，结果给了回调函数,执行回调
    task.append(obj)                                        # 把请求对象（socket对象）加入task延时任务列表

dlist = defer.DeferredList(task)                            # 创建循环，开始检测IO, 开始执行
dlist.addCallback(all_done)                                    # 给所有任务绑定一个回调函数，等所有的任务都结束了以后关闭连接,停止执行

reactor.run()                                                # 死循环检测deferred_list列表，如果有任务，马上开始执行任务