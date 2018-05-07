#!/usr/bin/env python
# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.autohome.com.cn/news/')
response.encoding = 'gbk'
# print(response.content)     # 拿到结果是字节类型，避免乱码
# response.encoding = 'gbk'
# print(response.text)        # 只拿文本信息，会乱码


# soup = BeautifulSoup(response.text, 'html.parser')
# tag = soup.find(id='auto-channel-lazyload-article')
# h3 = tag.find(name='h3', attrs={'class': 'xxx', 'id': 'xxx'})  # name是标签名字，attrs里面写属性
# print(h3)

soup = BeautifulSoup(response.text, 'html.parser')
li_list = soup.find(id='auto-channel-lazyload-article').find_all(name='li')

a = 0
for li in li_list:
    a += 1
    title = li.find('h3')
    if not title:
        continue
    summary = li.find('p').text
    url = li.find('a').get('href')  # 也可以这样取：li.find('a').attrs['href']
    img = li.find('img').get('src')
    print(title.text, url, summary, img)

    res = requests.get('http:' + img)
    # file_name = '%s.jpg' % (title.text,)
    file_name = a
    file_name = str(file_name) + '.jpg'
    with open(file_name, 'wb') as f:
        f.write(res.content)

