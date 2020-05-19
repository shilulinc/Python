# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"
'''
import sys

print(sys.path) #打印环境变量
print(sys.argv) #打印当前文件名称
'''

import os

cmd_res = os.popen("pwd").read()

print(cmd_res)

os.mkdir("new_dir")
