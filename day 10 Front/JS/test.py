#!/usr/bin/env python
# -*- coding utf-8 -*-

class Foo:
    def __init__(self, name):
        self.name = name
    def sayName(self):
        print(self.name)


obj1 = Foo('we')
obj1.sayName()
obj2 = Foo('wee')