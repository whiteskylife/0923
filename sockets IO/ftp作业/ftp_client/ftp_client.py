#!/usr/bin/env python
# -*- coding utf-8 -*-

import os
import json
import optparse


class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option('-s', '--server', dest='server', help='ftp server ip addr')
        parser.add_option('-p', '--port', dest='port', help='ftp server port')
        parser.add_option('-u', '--username', dest='username', help='ftp server username')
        parser.add_option('-P', '--password', dest='password', help='password')

    def interactive(self):
        pass