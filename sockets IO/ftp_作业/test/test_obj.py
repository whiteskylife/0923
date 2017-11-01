#!/usr/bin/env python
# -*- coding utf-8 -*-


class Foo:
    def __init__(self):
        self.name = 'whisky'

    def f1(self):
        print('f1 method')


class Son(Foo):
    def __init__(self):
        self.gender = 'male'

    def f1(self):
        print('%s is good guy' % self.name)


obj = Foo()
a = obj.gender
print(a)