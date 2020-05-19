#/usr/bin/env python
#_*_ coding:gbk _*_ # 此处声明文件为gbk编码格式，实际上python3内部默认的仍然是Unicode编码格式
__author__ = "Shi Lu"

import sys
print(sys.getdefaultencoding())

s = "您好"
print(s)
print(s.encode("gb2312")) # 转换成gb2312
print(s.encode()) # 默认转换成utf-8
print(type(s.encode()))

gb2312_to_utf8 = s.encode("gb2312").decode("gb2312").encode("utf-8")
print(gb2312_to_utf8)
