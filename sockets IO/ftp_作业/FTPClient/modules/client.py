#!/usr/bin/env python
# -*- coding utf-8 -*-

# ftp客户端主程序

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import socket
import json
import hashlib
import copy


class Clinet:

    def __init__(self, sys_argv):
        self.USER_HOME = '%s/var/users' % BASE_DIR
        self.args = sys_argv
        self.argv_parse()
        self.response_code = {
            '200': 'pass user authentication',
            '201': 'wrong username or password',
            '300': 'ready to get file from server',
            '301': 'ready to send to server',
            '302': 'file does not exist on ftp server',
            '303': 'storage is full',
            '601': 'changed directory',
        }
        self.handle()

    def handle(self):
        self.connect(self.ftp_host, self.ftp_port)
        if self.auth():
            self.interactive()      # 用户验证通过，开始交互

    def argv_parse(self):
        """
        参数解析函数,取出参数中的IP地址和端口
        :return:
        """
        if len(self.args) < 5:   # args[0] 是程序自身
            self.help_msg()
            sys.exit()
        else:
            mandatory_fields = ['-p', '-s']
            for i in mandatory_fields:
                if i not in self.args:
                    self.help_msg()
                    sys.exit('')
            try:
                self.ftp_host = self.args[self.args.index['-s'] + 1]
                self.ftp_port = int(self.args[self.args.index['-p'] + 1])
            except (IndexError, ValueError):
                self.help_msg()
                sys.exit()

    def connect(self, host, port):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
        except socket.error as e:
            sys.exit('Failed to connect server: %s' % e)

    def help_msg(self):
        """
        帮助信息
        :return:
        """
        msg = """
        wrong input...
        format： python ftp.py -s ftp_server_ip -p ftp_server_port
        """
        print(msg)

    def instruction_msg(self):
        """
        指令帮助信息
        :return:
        """
        msg = """
            get remote ftp_file
            put local remote
            ls
            cd  path
        """
        print(msg)

    def interactive(self):
        """
        交互函数，上传、下载等一系列操作
        :return:
        """
        self.logout_flag = False
        while self.logout_flag is not True:
            user_input = input('[%s]:%s' % (self.login_user, self.current_dir(self.cwd))).strip()  # 输入的命令信息，可能包括路径
            if len(user_input) == 0:
                continue
            status, user_input_instructions = self.parse_instruction(user_input)
            if status is True:
                func = getattr(self, 'instruction_' + user_input_instructions[0])  # user_input_instructions[0]是命令
                func(user_input_instructions)
            else:
                print('Invalid instruction. ')

    def instruction_ls(self, instructions):
        self.sock.sendall(('ls|%s' % json.dumps({})).encode())      # ? dunps 空？
        server_response = self.sock.recv(1024)
        print(str(server_response, 'gbk'))

    def instruction_dir(self, instructions):
        self.sock.sendall(('dir|%s' % json.dumps({})).encode())
        server_response = self.sock.recv(1024)
        print(str(server_response, 'gbk'))

    def instructions_cd(self, instructions):
        """
        :param instructions: 是命令列表
        :return:
        """
        if len(instructions) == 1:
            print('illegal instructions ')
        elif len(instructions) == 2:
            path = instructions[1]
            if path.startswith('/'):
                try_path = path.split('/')
            else:
                try_path = self.cwd         # 第一次取值时为空
                print('try_path', try_path)
                split_path = path.split('/')        # 实现cd多级目录功能，分割path/to/somewhere这种路径
                try_path.extend(split_path)
                print('try_path1', try_path)
            self.sock.sendall(('cd|%s' % json.dumps({'cwd': try_path})).encode())
            server_response = json.loads(self.sock.recv(1024).decode())
            if server_response['response'] == '601':
                print('self.cwd', server_response['cwd'])
                if server_response['cwd'][-1] == '..':
                    server_response['cwd'].pop(-1)
                    server_response['cwd'].pop(-1)
                self.cwd = server_response['cwd']           # cd命令，服务器端目录改变之后也要在客户端更改
            elif server_response['response'] == '602':
                print('directory does not exists ')

    def get_response_code(self, response):
        """
        处理服务器端返回的状态码信息
        :param response:
        :return:
        """
        response_code = response.split('|')
        code = response_code[1]
        return code

    def current_dir(self, cwd):
        return '/'.join(cwd) + '/'  # cwd为空时，join拼接不起来，只剩后面的'/'

    def auth(self):
        retry_count = 0
        while retry_count < 3:
            username = input('pls enter your username: ')
            if len(username) == 0:
                continue
            password = input('pls enter your password: ')
            if len(password) == 0:
                continue
            md5 = hashlib.md5()
            md5.update(password.encode())
            auth_str = 'user_auth|%s' % (json.dumps({'username': username, 'password': md5.hexdigest()}))
            self.sock.send(auth_str.encode())
            server_response = self.sock.recv(1024).decode()
            response_code = self.get_response_code(server_response)
            if response_code == '200':
                self.login_user = username
                self.cwd = ['']
                try:
                    os.makedirs('%s/%s' % (self.USER_HOME, self.login_user))
                except OSError:   # 已经创建文件夹，pass
                    print('user dir is existed')
                    pass
                return True
            else:
                # 验证失败
                retry_count += 1
        else:
            sys.exit('too many attemps')

    def parse_instruction(self, user_input):
        """
         ftp客户端用户输入的指令分析处理, 判断输入的方法是否存在程序中
        :param user_input:
        :return:
        """
        user_input_to_list = user_input.split()
        func_str = user_input_to_list[0]
        if hasattr(self, 'instruction_' + func_str):
            return True, user_input_to_list      # 如果类中包含输入的方法，返回True标志位，和输入的指令
        else:
            return False, user_input_to_list

