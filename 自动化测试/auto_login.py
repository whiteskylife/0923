#-*- coding:utf-8 -*-


__author__ = 'Administrator'
from selenium import webdriver      #  导入webdriver和time 类库
import time

#from

print "------软件测试自动化：登录界面测试用例------"
# 创建testClass 类


class testClass(object):

        def openB(self):
            """ 打开浏览器 """
            global browser  # 申明browser为全局变量
            browser = webdriver.Chrome()   # 实例化Firefox类
            time.sleep(3)   # 使程序暂停2秒，下同
            return "\n 已打开"

        def test(self, url):
            browser.get(url)    # get()方法打开url

        def keyinfo(self, url, unname, un, pwname, pw, authenticate_code, au):
            """定位用户名和密码输入框并写入数据"""
            browser.get(url)    # get()方法打开url
                # get()方法打开url
            time.sleep(0.1)             # 如果页面没有加载完成，继续向下执行可能会报错，要sleep几秒
            browser.find_element_by_id(unname).send_keys(un)  # 定位username输入框并使用send_keys()向其写入数据
            time.sleep(0.1)
            browser.find_element_by_id(pwname).send_keys(pw)  # 定位password输入框并使用send_keys()向其写入数据
            time.sleep(0.1)
            browser.find_element_by_id(authenticate_code).send_keys(au)
            browser.find_element_by_id('btn_login').click()
            time.sleep(1)
            browser.get('http://tnew.gxyclub.com/loanmanage/tyb_index?bieType=1')
            time.sleep(1)
            #browser.find_element_by_class_name('drop-down').click()
            #browser.find_element_by_class_name("invest-btn").click()
            browser.get('https://tnew.gxyclub.com/loanmanage/tyb_detail?id=361')

            browser.find_element_by_id('investAmount').send_keys(200)
            time.sleep(1)
            browser.find_element_by_class_name('m-btn').click()
            time.sleep(1)
            browser.find_element_by_class_name('t-affirm').click()
            time.sleep(2)
            #browser.find_element_by_name('password').send_keys(123456)
            browser.switch_to_window(browser.window_handles[1])
            time.sleep(3)
            browser.find_element_by_name('password').send_keys(123456)
            browser.find_element_by_class_name('submit-btn').click()
            time.sleep(1)
            #return {"test url": url, "Username": un, "Password": pw}

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
                screenshot = raw_input("需要截图以保留fail现象吗?(Y/N)(图片以LoginErro.jpg保留在C:\): ")  # 询问是否需截图
                if screenshot == "Y":
                    browser.save_screenshot("C:\LoginErro.jpg")     # 使用save_screenshot方法截图并以LoginErro保存
            else:   # 若页面title含某字符（即登录成功），则执行else语句
                print("O(∩_∩)O~登录成功")
            return "结束验证"

        def closeB(self):
            """关闭浏览器"""
            CloseB = raw_input("关闭?(Y/N): ")  # 询问是否需要关闭
            if CloseB == "Y":
                browser.quit()      # 使用quit()关闭
            return "\n ------本次测试用例运行结束，感谢使用，再见O(∩_∩)O~.------"


# 实例化testClass为 SucLogin：输入正确的用户名，密码，验证码登录
SucLogin = testClass()
print "1.打开浏览器", SucLogin.openB()
print "2.打开测试url，并输入用户名，密码"
#SucLogin.keyinfo("https://tnew.gxyclub.com/toLogin")
while True:
    time.sleep(2)
    SucLogin.keyinfo("https://tnew.gxyclub.com/toLogin", "userName", "fanqie", "password", "123456", 'authCode', '0000')
    browser.quit()
    time.sleep(2)
# print "3.请配合输入验证码\n", SucLogin.keyyzm("Yzm", "ValidCode")
# print "4.验证登陆是否成功\n", SucLogin.verifylogin("Submit", U"首页")
#print("5.关闭浏览器\n", SucLogin.closeB())

# 根据需要实例化testClass为XXXX，修改相关数据


# ……

