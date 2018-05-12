#!/usr/bin/env python
# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
asdf
    <div class="title">
        <b>The Dormouse's story总共</b>
        <h1>f</h1>
    </div>
<div class="story">Once upon a time there were three little sisters; and their names were
    <a  class="sister0" id="link1">Els<span>f</span>ie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</div>
ad<br/>sf
<p class="story">...</p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, features='lxml')
tag = soup.find(class_='story')
'''
print(tag)                  # 获取标签
print(tag.name)             # 获取标签名
print(tag.attrs)            # 获取属性，格式为字典
tag.attrs['kkk'] = 'vvvv'   # 通过操作字典，对属性进行修改
del tag.attrs['class']      # 删除操作


# children,所有子标签
for item in tag.children:
    print(type(item), item)

# children,所有子子孙孙标签
for item in tag.descendants:
    print(type(item), item)

# clear,将标签的所有子标签全部清空（保留标签名）
print(tag)
tag.clear()
print(tag)  # clear之后只剩下最外层标签

# decompose,递归的删除所有的标签
print(tag)
tag.decompose()
print(tag)  # 删除所有标签，包括最外层标签

# extract,递归的删除所有的标签，并获取删除的标签
print(tag)
taga = tag.find(name='a')
r = taga.extract()
print(tag)  # 删除所有标签，包括最外层标签
print('delete tag:', r)

# decode,转换为字符串（含当前标签）；decode_contents（不含当前标签）
print(tag.decode(), type(tag), type(tag.decode()))  # 输出：<class 'bs4.element.Tag'> <class 'str'> tag对象类型转换为字符串类型
print('-----'*20)
print(tag.decode_contents(), type(tag), type(tag.decode_contents()))  # <class 'bs4.element.Tag'> <class 'str'>

# encode,转换为字节（含当前标签）；encode_contents（不含当前标签）
print(tag.encode(), type(tag), type(tag.encode()))  # 输出： <class 'bs4.element.Tag'> <class 'bytes'> tag对象类型转换为bytes类型
print('-----'*20)
print(tag.encode_contents(), type(tag), type(tag.encode_contents()))  # <class 'bs4.element.Tag'> <class 'bytes'>



# find, 获取匹配的第一个标签
tag = soup.find('a')
print(tag)
tag = soup.find(name='a', attrs={'class': 'sister'}, recursive=True, text='Lacie') # recursive找子子孙孙
tag = soup.find(name='a', class_='sister', recursive=True, text='Lacie')      # class是python内部关键词，要class_这样写代表前端的class,
# print(tag)



# find_all,获取匹配的所有标签
tags = soup.find_all('a')
print(tags)

tags = soup.find_all('a',limit=1)
print(tags)

tags = soup.find_all(name='a', attrs={'class': 'sister'}, recursive=True, text='Lacie')
# tags = soup.find(name='a', class_='sister', recursive=True, text='Lacie')
print(tags)


# ####### 列表 #######
v = soup.find_all(name=['a','div'])
print(v)

v = soup.find_all(class_=['sister0', 'sister'])
print(v)

v = soup.find_all(text=['Tillie'])
print(v, type(v[0]))


v = soup.find_all(id=['link1','link2'])
print(v)

v = soup.find_all(href=['link1','link2'])
print(v)

# ####### 正则 #######  ***重要***
import re
p = re.compile('p')
p = re.compile('^p')
= soup.find_all(name=rep)
int(v)
rep = re.compile('sister.*')
v = soup.find_all(class_=rep)
print(v)

rep = re.compile('http://www.oldboy.com/static/.*')
v = soup.find_all(href=rep)
print(v)

# ####### 方法筛选 #######
def func(tag):
    return tag.has_attr('class') and tag.has_attr('id')
v = soup.find_all(name=func)        # 每找到一个标签就执行一次func函数
print(v)



# get,获取标签属性
tag = soup.find('a')
v = tag.get('id')
print(v)

# has_attr,检查标签是否具有该属性
tag = soup.find('a')
v = tag.has_attr('id')
print(v)

# get_text,获取标签内部文本内容，且是字符串类型的
print(tag)
print(tag.get_text())  # <class 'str'>,是字符串类型的


# index, 检查标签在某标签中的索引位置
tag = soup.find('body')
v = tag.index(tag.find('div'))
print(v)

tag = soup.find('body')
for i,v in enumerate(tag):
print(i,v)

# is_empty_element,是否是空标签(是否可以是空)或者自闭合标签，
#      判断是否是如下标签：'br' , 'hr', 'input', 'img', 'meta','spacer', 'link', 'frame', 'base'
tag = soup.find('br')
v = tag.is_empty_element
print(v)


# 当前的关联标签,内置属性，后面不加括号
# soup.next
# soup.next_element
# soup.next_elements
# soup.next_sibling
# soup.next_siblings
# 
# tag.previous
# tag.previous_element
# tag.previous_elements
# tag.previous_sibling
# tag.previous_siblings
# 
# tag.parent
# tag.parents

# 查找某标签的关联标签，可传参，参数和find和find_all中的参数是一样的，相当于二次筛选，可以写正则表达式、标签、属性
# tag.find_next(...)
# tag.find_all_next(...)
# tag.find_next_sibling(...)
# tag.find_next_siblings(...)

# tag.find_previous(...)
# tag.find_all_previous(...)
# tag.find_previous_sibling(...)
# tag.find_previous_siblings(...)

# tag.find_parent(...)
# tag.find_parents(...)

# 参数同find_all


# select,select_one, CSS选择器,前端的写法
soup.select("title")

soup.select("p nth-of-type(3)")

soup.select("body a")

soup.select("html head title")

tag = soup.select("span,a")

soup.select("head > title")

soup.select("p > a")

soup.select("p > a:nth-of-type(2)")

soup.select("p > #link1")

soup.select("body > a")

soup.select("#link1 ~ .sister")

soup.select("#link1 + .sister")

soup.select(".sister")

soup.select("[class~=sister]")   # class不等于sister的

soup.select("#link1")

soup.select("a#link2")

soup.select('a[href]')          # 具有href属性的a标签

soup.select('a[href="http://example.com/elsie"]')

soup.select('a[href^="http://example.com/"]')

soup.select('a[href$="tillie"]')

soup.select('a[href*=".com/el"]')  # 正则

# 标签的内容
# tag = soup.find('span')
# print(tag.string)          # 获取
# tag.string = 'new content' # 设置
# print(soup)

# tag = soup.find('body')
# print(tag.string)             # string既可以查看内容还能修改，text和get_text方法是只读的不能修改
# tag.string = 'xxx'
# print(soup)

# tag = soup.find('body')
# v = tag.stripped_strings  # 递归内部获取所有标签的文本,只读，无法设置
# print(v)

# append在当前标签内部追加一个标签
print(tag)
print('='*100)
taga = tag.find(class_='sister')
tag.append(taga)    # 对于一个存在的标签进行append操作，会移动这个标签进行append
print(tag)

# 创建标签并追加
print(tag)
print('='*100)
from bs4.element import Tag
obj = Tag(name='a')         # 创建一个标签进行append
obj.string = 'iam new'
obj.attrs['kkk'] = 'vvv'
tag.append(obj)
print(tag)


# insert在当前标签内部指定位置插入一个标签
from bs4.element import Tag
obj = Tag(name='i', attrs={'id': 'it'})
obj.string = '我是一个新来的'
tag = soup.find('body')
tag.insert(2, obj)      # 2是索引
print(soup)

# insert_after,insert_before 在当前标签后面或前面插入
from bs4.element import Tag
obj = Tag(name='i', attrs={'id': 'it'})
obj.string = '我是一个新来的'
tag = soup.find('body')
# tag.insert_before(obj)
tag.insert_after(obj)
print(soup)

# replace_with 在当前标签替换为指定标签
from bs4.element import Tag
obj = Tag(name='i', attrs={'id': 'it'})
obj.string = '我是一个新来的'
tag = soup.find('div')
tag.replace_with(obj)
print(soup)

# 创建标签之间的关系,不会改变位置，想要改变位置使用insert和append
# tag = soup.find('div')
# a = soup.find('a')
# tag.setup(previous_sibling=a)
# print(tag.previous_sibling)


# wrap，将指定标签把当前标签包裹起来
from bs4.element import Tag
obj1 = Tag(name='div', attrs={'id': 'it'})
obj1.string = '我是一个新来的'

tag = soup.find('a')
v = tag.wrap(obj1)
print(soup)

tag = soup.find('a')
v = tag.wrap(soup.find('p'))
print(soup)


# unwrap，去掉当前标签，将保留其包裹的标签

tag = soup.find('a')
v = tag.unwrap()
print(soup)

'''