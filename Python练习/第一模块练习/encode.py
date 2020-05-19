#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

import sys
print(sys.getdefaultencoding())

s = "您好"
print(s)
print(s.encode("gbk")) # 转换成gbk
print(s.encode()) # 默认转换成utf-8
print(type(s.encode()))

gbk_to_utf8 = s.encode("gbk").decode("gbk").encode("utf-8")
print(gbk_to_utf8)
