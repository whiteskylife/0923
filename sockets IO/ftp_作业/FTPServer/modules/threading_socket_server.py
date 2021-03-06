#!/usr/bin/env python
# -*- coding utf-8 -*-

import socketserver
import json
import os
from conf import settings
from modules import user
import hashlib
import subprocess
import platform


class MyTCPHandler(socketserver.BaseRequestHandler):

    response_code_list = {
        '200': 'Pass authentication ! ',
        '201': 'Wrong username or password !',
        '300': 'Ready to send file to client!',
        '301': 'Client ready to receive file',
        '302': 'File does not exist',
        '2002': 'ACK （可以开始上传）',
        '2003': 'file existed',
        '2004': 'continue put',
    }

    def handle(self):
        """
        重写handle方法
        :return:
        """
        while True:
            """
                # request：套接字对象，接收和发送数据。
                request, client_address = self.get_request()
                get_request方法:
                    self.socket.accept()
            """
            data = self.request.recv(1024).decode()
            print('received data:', data)
            if not data:
                print('user disconnected')
                break
            self.instruction_distributor(data)

    def instruction_distributor(self, instructions):
        """
        指令分发
        :param instructions: 客户端发送的指令信息
        :return:
        """
        print('in1', instructions)
        instructions = instructions.split('|')
        print('in2', instructions)

        function_str = instructions[0]      # 第一次接收数据，用户验证时：第一个参数user_auth，第二个参数：用户名、密码
        if hasattr(self, function_str):     # 有没有用户验证方法
            func = getattr(self, function_str)
            func(instructions[1])            # 此处仍是json格式
        else:
            print('Invalid instruction')

    def user_auth(self, data):
        """
        用户认证，检测用户名、密码，匹配成功：登录，返回状态码
        :param data: 用户、密码等信息（instructions[1]）
        :return:
        """
        auth_info = json.loads(data)        # 格式为字典
        if auth_info['username'] in settings.USER_ACCOUNT:   # 检测客户端发来的用户名是否在配置文件中
            if settings.USER_ACCOUNT[auth_info['uaername']]['password '] == auth_info['password']:  # 检测密码是否匹配
                self.login_user = user.User(auth_info['username'], settings.USER_ACCOUNT[auth_info['username']])
                # 实例化用户名，和用户名对应的密码，limit_storage
                response_code = '200'
            else:
                response_code = '201'
        else:
            response_code = '201'

        self.request.send('response|{0}'.format(response_code).encode())

    def ls(self, user_data):
        """
        ls 命令处理,区分平台处理
        :param user_data:
        :return:
        """
        directory_path = '%s\%s%s' % (settings.USER_HOME, self.login_user.username, '\\'.join(self.login_user.cwd) + '\\')
        # 确定当前目录，当客户端执行cd命令后，服务器端cd方法会在directory_path中的self.login_user.cwd添加对应路径
        print('cwd>>>>', directory_path)
        print('>>>', self.login_user.cwd)
        if platform.system() == 'Windows':
            cmd = 'dir %s' % directory_path
        else:
            cmd = 'ls %s' % directory_path
        print(cmd)
        cmd_call = subprocess.getoutput(cmd)
        cmd_result = bytes(cmd_call, encoding='gbk')
        self.request.sendall(cmd_result)

    def dir(self, user_data):
        directory_path = '%s\\%s%s' % (settings.USER_HOME, self.login_user.username, '\\'.join(self.login_user.cwd) + '\\')
        cmd = 'dir'
        cmd_call = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        cmd_result = cmd_call.stdout.read()
        self.request.sendall(cmd_result)

    def cd(self, user_data):
        """
        拼接绝对路径，判断绝对路径文件夹是否存在
        :param user_data:
        :return:
        """
        json_data = json.loads(user_data)
        new_dir = json_data['cwd']
        abs_dir = '%s\\%s%s' % (settings.USER_HOME, self.login_user.username, '\\'.join(new_dir))

        if os.path.isdir(abs_dir):
            self.request.sendall(json.dumps({'response': '601', 'cwd': new_dir}).encode())
            self.login_user.cwd = new_dir
        else:
            self.request.sendall(json.dumps({'response': '602'}).encode())

