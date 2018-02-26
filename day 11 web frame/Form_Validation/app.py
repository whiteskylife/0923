#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import re
# form验证：要求前端name字段和后端类中封装的字段名字一致
# checkbox验证
# 文件名验证匹配不支持中文汉字


class IPFiled:
    REGULAR = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"   # 静态 字段

    def __init__(self, error_dict=None, required=True):
        """
        :param error_dict: 自定义显示用户输入错误
        :param required:   默认表示必须要填值
        """
        # 封装了错误信息 ，如果没有传入一个包含错误信息的字典，则使用默认，如果有则覆盖默认
        self.error_dict = {}
        if error_dict:  # 81 行实例化 传入的错误信息,如果不传 则为None,则不会执行
            self.error_dict.update(error_dict)  # 将实例化时候 传入的错误信息封装

        self.required = required # # 81 行实例化 传入的是否为空字段,默认是浏览器输入不许为空

        self.error = None   # 错误信息
        self.value = None   # 匹配的值是什么
        self.is_valid = False   # 是否匹配

    def validate(self, name, input_value):
        """
        :param name: 字段名
        :param input_value: 用户表单中输入的内容
        :return:
        """
        if not self.required: # 当比如81行我们传入可以为空的时候即False时候走这一段代码  # 翻译：如果 没有 内容： 即如果输入空（not这里不能翻译为不，要翻译为没有）
            # 用户输入允许为空
            self.is_valid = True      # 设置封装值为真，表示验证通过
            self.value = input_value  # 将空值封装
        else:       # 当81行要求输入不为空时候 翻译：否则，如果 有 内容，即不为空时
            # 用户有输入要求不允许为空,这一要验证正则了。
            if not input_value.strip():  # 输入为空,返回错误信息。 错误信息字典
                if self.error_dict.get('required', None):  # 81行定义的错误信息。如果未定义则自己定义
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name     # 默认错误信息
            else:           # 用户输入不为空,
                ret = re.match(IPFiled.REGULAR, input_value)  # 获取 静态字段的正则字符串,跟用户的input输入内容匹配
                if ret:     # 匹配通过,
                    self.is_valid = True
                    self.value = input_value    # self.value = ret.group()也是一样的
                else:  # 匹配不通过,返回错误字典
                    if self.error_dict.get('valid', None): #81 行定义的错误信息,如果未定义则自己定义
                        self.error = self.error_dict['valid']
                    else:
                        self.error = "%s is invalid" % name


class StringFiled:
    REGULAR = "(.*)"  # 静态 字段

    def __init__(self, error_dict=None, required=True):
        """
        :param error_dict: 自定义显示用户输入错误
        :param required:   默认表示必须要填值
        """
        # 封装了错误信息 ，如果没有传入一个包含错误信息的字典，则使用默认，如果有则覆盖默认
        self.error_dict = {}
        if error_dict:  # 81 行实例化 传入的错误信息,如果不传 则为None,则不会执行
            self.error_dict.update(error_dict)  # 将实例化时候 传入的错误信息封装

        self.required = required # # 81 行实例化 传入的是否为空字段,默认是浏览器输入不许为空

        self.error = None   # 错误信息
        self.value = None   # 匹配的值是什么
        self.is_valid = False   # 是否匹配

    def validate(self, name, input_value):
        """
        :param name: 字段名
        :param input_value: 用户表单中输入的内容
        :return:
        """
        if not self.required: # 当比如81行我们传入可以为空的时候即False时候走这一段代码  # 翻译：如果 没有 内容： 即如果输入空（not这里不能翻译为不，要翻译为没有）
            # 用户输入允许为空
            self.is_valid = True      # 设置封装值为真，表示验证通过
            self.value = input_value  # 将空值封装
        else:       # 当81行要求输入不为空时候 翻译：否则，如果 有 内容，即不为空时
            # 用户有输入要求不允许为空,这一要验证正则了。
            if not input_value.strip():  # 输入为空,返回错误信息。 错误信息字典
                if self.error_dict.get('required',None):  # 81行定义的错误信息。如果未定义则自己定义
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name     # 默认错误信息
            else:  # 用户输入不为空,
                ret = re.match(IPFiled.REGULAR, input_value) #获取 静态字段的正则字符串,跟用户的input输入内容匹配
                if ret: # 匹配通过,
                    self.is_valid = True
                    self.value = input_value    # self.value = ret.group()也是一样的
                else:  # 匹配不通过,返回错误字典
                    if self.error_dict.get('valid', None): #81 行定义的错误信息,如果未定义则自己定义
                        self.error = self.error_dict['valid']
                    else:
                        self.error = "%s is invalid" % name


class CheckBoxFiled:
    """
    不做正则匹配，只需看列表中是否有值
    """
    def __init__(self, error_dict=None, required=True):
        """
        :param error_dict: 自定义显示用户输入错误
        :param required:   默认表示必须要填值
        """
        # 封装了错误信息 ，如果没有传入一个包含错误信息的字典，则使用默认，如果有则覆盖默认
        self.error_dict = {}
        if error_dict:  # 81 行实例化 传入的错误信息,如果不传 则为None,则不会执行
            self.error_dict.update(error_dict)  # 将实例化时候 传入的错误信息封装

        self.required = required # # 81 行实例化 传入的是否为空字段,默认是浏览器输入不许为空

        self.error = None   # 错误信息
        self.value = None   # 匹配的值是什么
        self.is_valid = False   # 是否匹配

    def validate(self, name, input_value):
        """
        :param name: 字段名：favor
        :param input_value: 用户选中的值 如[1, 2]，或者为None
        :return:
        """
        if not self.required: # 当比如81行我们传入可以为空的时候即False时候走这一段代码  # 翻译：如果 没有 内容： 即如果输入空（not这里不能翻译为不，要翻译为没有）
            # 用户输入允许为空
            self.is_valid = True      # 设置封装值为真，表示验证通过
            self.value = input_value
        else:       # 不允许为空 翻译：否则，如果 有 内容，即不为空时
            if not input_value:  # 输入为空,返回错误信息。 错误信息字典
                if self.error_dict.get('required', None):  # 81行定义的错误信息。如果未定义则自己定义
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name     # 默认错误信息
            else:  # 用户输入不为空
                self.is_valid = True
                self.value = input_value


class FileFiled:
    REGULAR = "^(\w+\.pdf)|(\w+\.mp3)|(\w+\.py)|(\w+\.txt)$"  # 静态 字段

    def __init__(self, error_dict=None, required=True):
        """
        :param error_dict: 自定义显示用户输入错误
        :param required:   默认表示必须要填值
        """
        # 封装了错误信息 ，如果没有传入一个包含错误信息的字典，则使用默认，如果有则覆盖默认
        self.error_dict = {}
        if error_dict:  # 81 行实例化 传入的错误信息,如果不传 则为None,则不会执行
            self.error_dict.update(error_dict)  # 将实例化时候 传入的错误信息封装

        self.required = required  # 81 行实例化 传入的是否为空字段,默认是浏览器输入不许为空

        self.error = None   # 错误信息
        self.value = []   # 匹配的值是什么
        self.is_valid = True
        self.name = None
        self.success_file_name_list = []

    def validate(self, name, all_file_name_list):
        """
        :param name: 字段名
        :param all_file_name_list: 所有文件的文件名
        :return:
        """
        self.name = name            # 上传文件的字段名fafafa
        if not self.required:
            # 用户输入允许为空
            self.is_valid = True      # 设置封装值为真，表示验证通过
            self.value = all_file_name_list
        else:
            if not all_file_name_list:
                self.is_valid = False
                if self.error_dict.get('required', None):
                    self.error = self.error_dict['required']
                else:
                    self.error = "%s is required" % name
            else:
                # 循环所有文件名
                for file_name in all_file_name_list:
                    ret = re.match(FileFiled.REGULAR, file_name)        # 文件名中含有中文无法匹配
                    if not ret:
                        self.is_valid = False       # 验证没有通过
                        if self.error_dict.get('valid', None):
                            self.error = self.error_dict['valid']
                        else:
                            self.error = "%s is invalid" % name
                        break
                    else:  # 可能会上传多个文件，有一个文件正确就加入文件列表
                        self.value.append(file_name)

    def save(self, request, path='statics'):
        """
        :param request: request中封装了所有用户发过来的前端中的数据
        :param path:
        :return:
        """
        file_metas = request.files.get(self.name)      # 所有文件列表,self.name取前端的name变量值,get得到文件列表[{文件1}, {文件2}]
        # print(self.name)        # 输出fafafa
        # print(file_metas)
        for meta in file_metas:                     # 循环文件列表，列表中包含很多字典，每个字典包含一个文件，meta为单个字典
            print('meta in for loop---', meta)
            file_name = meta['filename']
            import os
            new_file_name = os.path.join(path, file_name)
            if file_name and file_name in self.value:       # 文件名为空不上传，且文件名要在成功的列表中才会上传保存
                with open(new_file_name, 'wb') as up:
                    up.write(meta['body'])                  # 字典中的body字段包含文件内容
        # print(file_metas)输出
        # [{'body': b'1', 'content_type': 'text/plain', 'filename': '21.txt'},
        # {'body': b'1', 'content_type': 'text/plain', 'filename': '12.txt'}]
        # print('meta in for loop---', meta)输出
        # meta in for loop - -- {'body': b'1', 'content_type': 'text/plain', 'filename': '21.txt'}
        # meta in for loop - -- {'body': b'1', 'content_type': 'text/plain', 'filename': '12.txt'}


class BaseForm:
    def check_valid(self, handle):
        """
         获取用户提交的数据，将用户提交的数据传递到对应的类中进行正则表达式匹配，再调用类中匹配结果和正确/错误等自定义信息
        :param handle: post方法中的self，里面封装了get_argument方法，可以直接取前端传过来的参数值
        :return:返回正则匹配结果：成功-True；失败：false，正则匹配成功后返回一个字典，失败返回错误信息
        """
        flag = True
        error_message_dict = {}
        success_value_dict = {}
        for key, regular in self.__dict__.items():    # 遍历self中封装的参数
            # key是host、ip、port、phone
            # regular:当调用HomeForm类时值为IPField(required=True)对象
            if type(regular) == CheckBoxFiled:      # 复选框功能
                # print('question：--------' + str(type(regular)))
                # print('question：--------' + str(CheckBoxFiled))
                input_value = handle.get_arguments(key)  # 对于CheckBox来说，input_value就是用户提交name="favor"的列表
            elif type(regular) == FileFiled:             # 文件上传功能，获取文件名,放入一个列表中
                file_list = handle.request.files.get(key)  # [{'body':'xx', 'filename':'xx'},{'body':'xx', 'filename':'xx'}]
                # print(file_list)
                input_value = []
                if file_list:       # 如果没有提交文件，会报错，此处用个if避免报错
                    for item in file_list:
                        input_value.append(item['filename'])    # 加入列表，由validate方法进行所有文件名验证
            else:                                       # 输入内容功能
                input_value = handle.get_argument(key)
                # print(input_value + '输入内容功能==========')
            # 将具体的验证放在validate方法中
            regular.validate(key, input_value)  # regular为每次循环时HomeForm类中封装的对象
            if regular.is_valid:        # 如果正则匹配成功（调用IPField中封装的字段）
                success_value_dict[key] = regular.value         # 把匹配到的值放到字典中
            else:
                error_message_dict[key] = regular.error         # 把错误信息放到字典中
                flag = False                                    # HomeForm类中，有一种对象不符合正则匹配，就返回失败
        return flag, success_value_dict, error_message_dict


class IndexForm(BaseForm):
    def __init__(self):
        self.host = "(.*)"
        self.ip = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"
        self.port = '(\d+)'
        self.phone = '^1[3|4|5|8][0-9]\d{8}$'


class HomeForm(BaseForm):
    def __init__(self):
        self.ip = IPFiled(required=True, error_dict={'required': '不能为空...', 'valid': '格式错误了'})
        self.host = StringFiled(required=False)
        self.favor = CheckBoxFiled(required=True, error_dict={'required': '必须选择一个...', 'valid': '格式错误了'})      # 验证成功后，favor中的数据为用户选择列表
        self.fafafa = FileFiled(required=True)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self, *args, **kwargs):
        obj = IndexForm()
        is_valid, success_dict, error_dict = obj.check_valid(self)
        if is_valid:
            print(value_dict)


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html', error_dict=None)

    def post(self, *args, **kwargs):
        # files = self.request.files.get('fafafa', [])        # 表示获取提交过来的所有文件，如[文件1， 文件2]，前端文件name相同

        obj = HomeForm()
        is_valid, success_dict, error_dict = obj.check_valid(self)
        if is_valid:            # 如果HomeForm类中所有对象校验成功
            print('success', success_dict)
            obj.fafafa.save(self.request)   # self.request中封装了所有用户发过来的前端中的数据
        else:
            print('error', error_dict)
            self.render('home.html', error_dict=error_dict)     # 错误信息传递给前端渲染


settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/home", HomeHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()











