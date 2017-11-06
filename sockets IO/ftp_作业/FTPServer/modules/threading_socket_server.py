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
        print('in1', instructions)
        instructions = instructions.split('|')
        print('in2', instructions)

        function_str = instructions[0]
        if hasattr(self, function_str):
            func = getattr(self, function_str)
            func(instructions[1])
        else:
            print('Invalid instruction')