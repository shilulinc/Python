# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

# 第一种方式：
# import module_alex  -->  相当于把module_alex的所有的代码解释一遍赋值给module_alex，调用时用moudle_alex.name
# 或者module_alex.logger()
# module1.say_hello()

# 第二种方式：
# from module_alex import name   -->  相当于把module_alex中的name导入当前位置执行一遍，调用时直接name就可以
# print(module1.name)

"""
from module_alex import name,logger
print(name)
logger()
"""

# from module_alex import *  # 导入所有代码在此程序中执行一次，不建议使用

"""
from module_alex import logger as logger_alex
def logger():
    print("in the main")

logger()
logger_alex()
"""
import sys,os
print(sys.path)
print(os.path.abspath(__file__))  # 打印文件的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))  # 打印文件的父目录
x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)
import module_alex
