#!/usr/bin/env python
# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

# 获取token
r1 = requests.get('https://github.com/login')
s1 = BeautifulSoup(r1.text, 'html.parser')
token = s1.find(name='input', attrs={'name': 'authenticity_token'}).get('value')
r1_cookie_dict = r1.cookies.get_dict()      # github在你第一次发get请求时就会返回给你cookie信息
# print(token)

# 将用户名密码token发送到服务端
"""
commit:Sign in
utf8:✓
authenticity_token:V+T/saccB1A2HRycwadZuWR3dL8lnj5LIvANGQbPNClUs36niDyDT7diXSqIBfcaZ4u5FAvCbZKNA/efDjPqyw==
login:123
password:123
"""
r2 = requests.post(
    'https://github.com/session',
    data={
        'utf8': '✓',
        'authenticity_token': token,
        'login': '',
        'password': '',
        'commit': 'Sign in',
    },
    cookies=r1_cookie_dict,
)
# print(r2.text)
r2_cookie_dict = r2.cookies.get_dict()

# 合并cookie登录后访问其他页面全部携带过去验证
cookie_dict = {}
cookie_dict.update(r1_cookie_dict)
cookie_dict.update(r2_cookie_dict)

r3 = requests.get(
    url='https://github.com/settings/emails',
    cookies=cookie_dict,
)


print(r3.text)