#!/usr/bin/env python
# -*- coding utf-8 -*-

'''
li = []

for i in range(10):
    def f1():
        return i
    li.append(f1)
    # 相当于 li.append(lambda: i)
print(i)

print(li)
print(li[0]())
print(li[1]())



def xo():
    return x

相当于： lambda:x
'''


li = [lambda:x for x in range(9)]
print(li)
print(li[1]())      # 此处才开始调用列表中的函数，此时x的值已经循环到8了


# 小结：函数只有在被调用时才会执行