#!/usr/bin/env python
# -*- coding utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import random,time


browser = webdriver.Chrome() #启动chrome浏览器
time.sleep(3) #停顿3秒
browser.maximize_window() #浏览器窗口最大化

OutputLogin = Login(browser,username, password) #登录网页的函数，后续讲解

time.sleep(int(random.uniform(1, 10)))#随机产生一个1到9秒的随机整数，然后等待这个时间

browser.quit() #退出浏览器
    def Login(browser,username, password):
        browser.get('tnew.gxyclub.com') #浏览器登录网页的URL
        time.sleep(3)
        try:
        # find user login input box
        elem_user=browser.find_element_by_id("username")
        # 这个是通过find_element_by_id函数来寻找定位网页上的id为username的控件
        elem_user.clear()
        elem_user.send_keys(username)

        # 然后向这个控件发送username的值
        time.sleep(1)
        # find pwd input box
        elem_pwd = browser.find_element_by_id("password")
        elem_pwd.clear()
        elem_pwd.send_keys(password)
        time.sleep(1)
        # enter RETURN in pwd box to activate
        elem_pwd.send_keys(Keys.RETURN) # 然后向这个控件发送回车键，注意，如果是键盘上的回车，SHIFT，CONTROL键之类的，要用Keys.控制键的名称作为输入。
        return username+'login successfully \n'
        except:
        return username+" login failed \n"
        pass