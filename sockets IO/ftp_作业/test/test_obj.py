#!/usr/bin/env python
# -*- coding utf-8 -*-


class Foo:
    def f1(self):
        print('f1 method')

    def f2(self):
        print(self.sock)


class Son(Foo):
    def __init__(self):
        self.sock = 'Son socket'

    def f1(self):
        print('%s is good guy' % self.name)


obj = Son()
obj.f1()