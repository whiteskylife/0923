#!/usr/bin/env python
# -*- coding utf-8 -*-
# -*- coding:cp936 -*-
__author__ = 'Administrator'
# 导入webdriver和time 类库
from selenium import webdriver
import time

print("------软件测试自动化：登录界面测试用例------")
# 创建testClass 类


class testClass(object):

        def openB(self):
            """ 打开浏览器 """
            global browser  # 申明browser为全局变量
            browser = webdriver.Chrome()   # 实例化Firefox类
            time.sleep(2)   # 使程序暂停2秒，下同
            return "\n 已打开"

        def keyinfo(self, url, unname, un, pwname, pw, authenticate_code, au):
            """定位用户名和密码输入框并写入数据"""
            browser.get(url)    # get()方法打开url
            time.sleep(2)
            browser.find_element_by_name(unname).send_keys(un)  # 定位username输入框并使用send_keys()向其写入数据
            time.sleep(2)
            browser.find_element_by_name(pwname).send_keys(pw)  # 定位password输入框并使用send_keys()向其写入数据
            time.sleep(2)
            browser.find_element_by_name(authenticate_code).send_keys(au)

            return {"test url": url, "Username": un, "Password": pw}

        def keyyzm(self, yzmname, yzmpicid):
            """定位验证码输入框和图片，在用户协助下输入验证码，可根据需要切换图片"""
            # ChangeReq = input("看不清验证码图片，需切换?(Y/N): ", )    # 询问用户是否能看清验证码图片
            # while ChangeReq == "Y":
            #     browser.find_element_by_id(yzmpicid).click()    # 若用户无法看清，则定位验证码图片元素并点击直到用户看清
            #     clearPic = input("可以看清图片吗?(Y/N): ", )   # 询问用户是否能看清
            #     if clearPic == "Y":     # 若能看清，则不在切换图片
            #         ChangeReq = "N"
            # yzm = input("请输入看到的验证码:", )     # 用户输入验证码
            # browser.find_element_by_name(yzmname).send_keys(yzm)  # 定位验证码输入框并写入数据
            # return yzm

        def verifylogin(self, buttonname, title):
            """点击登录按钮，并验证是否登录成功（验证依据：登录后的页面源代码title中所含字符信息）"""
            browser.find_element_by_name(buttonname).click()  # 定位登录按钮并点击
            time.sleep(1)
            try:
                assert title in browser.title  # 使用assert断言页面title含某字符
            except AssertionError:  # 若页面title不含某字符（即登录失败），则引发AssertionError
                print("%>_<% ...登陆失败") # AssertionError 的处理方式
                screenshot = input("需要截图以保留fail现象吗?(Y/N)(图片以LoginErro.jpg保留在C:\): ")  # 询问是否需截图
                if screenshot == "Y":
                    browser.save_screenshot("C:\LoginErro.jpg")     # 使用save_screenshot方法截图并以LoginErro保存
            else:   # 若页面title含某字符（即登录成功），则执行else语句
                print("O(∩_∩)O~登录成功")
            return "结束验证"

        def closeB(self):
            """关闭浏览器"""
            CloseB = input("关闭?(Y/N): ")  # 询问是否需要关闭
            if CloseB == "Y":
                browser.quit()      # 使用quit()关闭
            return "\n ------本次测试用例运行结束，感谢使用，再见O(∩_∩)O~.------"

time.sleep(5)

# 实例化testClass为 SucLogin：输入正确的用户名，密码，验证码登录

SucLogin = testClass()
print("1.打开浏览器", SucLogin.openB())
print("2.打开测试url，并输入用户名，密码\n",)
SucLogin.keyinfo("https://tnew.gxyclub.com/toLogin", "userName", "ltest1", "password", "123456", 'authCode', '0000')

# print "3.请配合输入验证码\n", SucLogin.keyyzm("Yzm", "ValidCode")
# print "4.验证登陆是否成功\n", SucLogin.verifylogin("Submit", U"首页")
print("5.关闭浏览器\n", SucLogin.closeB())

# 根据需要实例化testClass为XXXX，修改相关数据


# ……

