# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

"""
# 优化前：
import module_test

def logger():
    module_test.test()
    print("in the logger")

def search()
    module_test.test()
    print("in the search")

"""

"""
# 优化后：
from module_test import test  # 可以加as取个别名

def logger():
    test()
    print("in the logger")

def search()
    test()
    print("in the search")

"""
