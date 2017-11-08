#!/usr/bin/env python
# -*- coding utf-8 -*-

import subprocess

command = input('input cmd: ')
cmd_call = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
cmd_result = cmd_call.stdout.read()
print(str(cmd_result))