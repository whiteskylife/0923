#!/usr/bin/env python
# -*-coding:utf-8 -*-

import requests
# 1. 调用关系
# requests.get()
# requests.post()
# requests.put()
# requests中的方法如：上面的方法，全部调用下面的request方法
# requests.request('post')

# 2.常用参数
requests.get(                        # get请求中没有data参数，data是请求体
    url='xxx',
    params={'k1': 'v1', 'nid': 888},  # params：在url上面进行传参，get方式传参
    cookies={},
    headers={}                      # 设置请求头
)

# http://www.baidu.com?k1=v2&nid=888

# requests.post(
#     url='xxx',
#     params={'k1':'v1','nid':888},
#     cookies={},
#     headers={},
#     data={},
#     json={}           #和data相同，区别：内部帮你序列化
# )

# 注意： 请求头，请求头设置不当服务器端可能拿不到值
# Content-Type:application/x-www-form-urlencoded,
# 在POST请求时设置这个请求头,request.POST在携带application/x-www-form-urlencoded这个请求头才能拿到数据

# requests.post(url='',data={},headers={'content-type': 'application/json'}) # application/json
# requests.post(url='',data={},headers={'content-type': 'application/json'})
# requests.post(url='',json={})  # json默认携带：{'content-type': 'application/json'}这个头
# data参数默认携带有Content-Type:application/x-www-form-urlencoded这个头

# def param_auth():
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
# HTTPBasicAuth,HTTPDigestAuth两种约定俗成验证规则，本质都是在请求头中加入认证信息
# ret = requests.get("http://192.168.1.1", auth=HTTPBasicAuth('wupeiqi', 'sdfasdfasdf'))
# ret = requests.get("http://192.168.1.1", auth=HTTPDigestAuth('wupeiqi', 'sdfasdfasdf'))
# ret = requests.get("http://192.168.1.1", headers={'Authorization': "asdfasdfasdfasf"})    # 本质都是在请求头中加入认证信息
# print(ret.text)


# allow_redirects是否允许跳转
# response = requests.get('http://www.adc.com',allow_redirects=True)        # 默认get方法中允许跳转
# print(response.text) # http://www.adc.com
# print(response.text) # http://www.baidu.com



# stream参数，爬取大文件，边爬编写
# response = requests.get('url',stream=True)
# with open('') as f:
#     f.write('xxx')
# for line in response.iter_content():
#     pass
# response.close()              # 手动关闭连接
#
# from contextlib import closing
# with closing(requests.get('http://httpbin.org/get', stream=True)) as r:       # 自动关闭连接，r代表响应
#     # 在此处理响应。
#     for i in r.iter_content():
#         print(i)


# 证书：
# verify 默认True，携带
#     :param verify: (optional) Either a boolean, in which case it controls whether we verify
#             the server's TLS certificate, or a string, in which case it must be a path
#             to a CA bundle to use. Defaults to ``True``
# 知乎，可带可不带，【知乎，xxxx】
# requests.get('http://httpbin.org/get', stream=True,cert="xxxx.pem")  # cert:本地证书路径

# 请求头、响应头，响应体，都包含什么参数？ User-Agent是在哪













