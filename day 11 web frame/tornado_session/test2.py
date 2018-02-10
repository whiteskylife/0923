#!/usr/bin/env python
# -*-coding utf-8 -*-


class A:
    def bar(self):
        print(self)
        print('BAR')
        self.f1()

    def f1(self):
        print('B')


class B(A):
    def f1(self):
        print('B')


class C:
    def f1(self):
        print(self, "in f1")
        print('C')


class D(C, B):
    pass


d1 = D()
d1.bar()


# 输出：
# BAR
# C
