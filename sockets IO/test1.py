# -*- coding: utf-8 -*-
import threading
import time


def process(arg):
    time.sleep(1)
    print(arg)

for i in range(1, 10):
    t = threading.Thread(target=process, args=(i,))
    t.start()