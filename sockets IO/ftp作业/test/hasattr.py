# -*- coding: utf-8 -*-

import test


inp = input('guess it:')
if hasattr(test.Common, inp):
    print('your modules exists')
else:
    print('it isnot exists')

