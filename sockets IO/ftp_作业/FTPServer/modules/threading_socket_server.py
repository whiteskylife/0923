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
            data = self.request.recv(1024).decode()
            print('received data:', data)
            if not data:
                print('user disconnected')
                break


