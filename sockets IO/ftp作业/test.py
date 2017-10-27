# -*- coding: utf-8 -*-

# 利用反射

class Common:

    def __init__(self):
        self.name = 'alex'
        self.gender = 'male'

    def f1(self):
        print('this is method f1')

    def f2(self):
        print('this is method f2')
        if hasattr(self, 'start'):
            print('11111111111111111')
        else:
            print('22222222222222222')

    def start(self):
        print('this is start method')


obj = Common()
obj.f2()
