#!/usr/bin/env python
# -*-coding utf-8 -*-
import time
import hashlib

container = {}
obj = hashlib.md5()
obj.update(bytes(str(time.time()), encoding='utf-8'))
rand_str = obj.hexdigest()


container[rand_str] = {}   # 设置value为字典,value即为用户信息，即为session
container[rand_str]['alex'] = '111'
print(container)
print(container.keys())

# set_cookie(key, value)

# container = { value : { '用户信息': '111'}}

# {'87ba085c5f01c3e28969c05af466fae6': {'alex': '111'}}
# { cookie字符串：                     { 用户信息，session  }}


