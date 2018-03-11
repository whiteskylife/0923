#!/usr/bin/env python
# -*-coding:utf-8 -*-


class Father:
    def call_children(self):
        child_method = getattr(self, 'out')
        child_method()

    def print(self):
        child_method = getattr(self, 'in_child')
        print('%s oooooooooo' % child_method )


class Children(Father):
    in_child = 'i am child'

    def out(self):
        print('hehe')


obj = Children()

obj.print()