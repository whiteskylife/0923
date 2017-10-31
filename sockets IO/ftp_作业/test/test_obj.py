#!/usr/bin/env python
# -*- coding utf-8 -*-


class Foo:

    def __init__(self):
        self.name = 'whisky'
        self.age = '26'
        self.gender = 'male'

    def f1(self):
        print('f1 method')

    def f2(self):
        print('f2 method')

obj = Foo()
a = obj.name
b = obj.age
print(a, b)
