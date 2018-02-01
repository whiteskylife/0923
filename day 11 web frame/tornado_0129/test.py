#!/usr/bin/env python
# -*-coding utf-8 -*-
# 拼接列表中的字符串
li = []

temp = '<a href="/index/1">1</a>'
for i in range(5):
    li.append(temp)

print(li)

li1 = "".join(li)
print(li1)