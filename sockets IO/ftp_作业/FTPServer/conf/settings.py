#!/usr/bin/env python
# -*- coding utf-8 -*-

import os
import sys
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_HOME = '%s\\var\\users' % BASE_DIR

USER_ACCOUNT = {
    'alex': {
        'password': 'e10adc3949ba59abbe56e057f20f883e',
        'storage_limit': 2097152
    },
    'whisky': {
      'password': '202cb962ac59075b964b07152d234b70',
      'storage_limit': 2097152
    },

}

