#!/usr/bin/env python
# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
"""
phone:8617748672617
password:qweqwe
oneMonth:1
"""
head = {}
requests.request()
# 写入User Agent信息
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
# r0 = requests.Request('http://dig.chouti.com/', headers=head)
r0 = requests.get('http://dig.chouti.com/', headers=head)
# r0_cookie_dict = r0.cookies.get_dict()
print(r0.text)
# print(r0_cookie_dict)
r1 = requests.post(
    'https://dig.chouti.com/login',
    data={
        'phone': '8617748672617',
        'password': '',
        'oneMonth': 1,
    },
    headers=head
    # cookies=r0_cookie_dict
)
print(r1.text)