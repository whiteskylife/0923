#!/usr/bin/env python
# -*- coding utf-8 -*-

import socketserver
import json

from conf import settings
from modules import user
import hashlib
import subprocess


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
        指令分发函数
        :param instructions: 客户端发送的指令信息
        :return:
        """
        print('in1', instructions)
        instructions = instructions.split('|')
        print('in2', instructions)

        function_str = instructions[0]      # 第一个参数user_auth，第二个参数：用户名、密码
        if hasattr(self, function_str):     # 有没有用户验证方法
            func = getattr(self, function_str)
            func(instructions[1])           # 此处仍是json格式
        else:
            print('Invalid instruction')

    def user_auth(self, data):
        """
        用户认证
        :param data: 用户、密码等信息（instructions[1]）
        :return:
        """
        auth_info = json.loads(data)        # 格式为字典
        if auth_info['username'] in settings.USER_ACCOUNT:   # 检测客户端发来的用户名是否在配置文件中
            if settings.USER_ACCOUNT[auth_info['uaername']]['password '] == auth_info['password']:
                #本地文件存储的密码和客户端发来的密码比对
                self.login_user =

    def login_user(self):
        pass