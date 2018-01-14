#!/usr/bin/env python
# -*-coding:utf-8 -*-


def new():
    return "new"


def index():
    return "index"


URLS = {
    '/new': new,
    '/index': index,
}


st = '/new'

if st in URLS.keys():
    val = URLS[st]
    ret = val()
    print ret
