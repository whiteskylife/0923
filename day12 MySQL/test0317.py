#!/usr/bin/env python
# -*-coding:utf-8 -*-
import random

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
d = random.randint(1, 100)

while True:

    if a + b == 8 and c - d == 6 and a + c == 13 and b + d == 8:
        print(a, b, c, d)
