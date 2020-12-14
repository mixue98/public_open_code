# -*- coding: utf-8 -*-
# @file: Specify_MD5.py
# @time: 2020/11/2711:08
# @Site: 
# @Software: PyCharm
# 指定文件得到它的文件MD5值

import sys
import hashlib
import os.path

# filename = sys.argv[1]
filename = 'E:\\mycode\\list\\hema.apk'

if os.path.isfile(filename):
  fp=open(filename,'rb')
  contents=fp.read()
  fp.close()
  print(hashlib.md5(contents).hexdigest())
else:
  print('file not exists')

