#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

# 文件修改有两种方法：1.不能在硬盘中修改，否则会覆盖原文件，使用vim读到内存中 2.同时打开两个文件，从旧文件中一行一行读取内容写到
# 新文件，读到需要修改的行时修改内容继续写到新文件

# example
"""
f = open("yesterday", "r", encoding="utf-8")
f_new = open("yesterday_new", "w", encoding="utf-8")

for line in f:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受", "肆意的快乐等Alex享受")
    f_new.write(line)
f.close()
f_new.close()
"""

# practice
# 实现简单的shell sed替换功能

import sys

f = open("yesterday", "r", encoding="utf-8")
f_new = open("yesterday_new", "w", encoding="utf-8")

find_str = sys.argv[1]
replace_str = sys.argv[2]
for line in f:
    if find_str in line:
        line = line.replace(find_str, replace_str)
    f_new.write(line)
f.close()
f_new.close()
