# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

print("from the package package_test")

# import test1  # test1 = "test1.py all code"  调用：.test1.test()

from . import test1
# 相当于找到test1文件并在当前路径执行一遍：
"""
def test():
    print("in the test")
"""