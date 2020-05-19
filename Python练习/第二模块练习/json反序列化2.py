# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

"""
# json是所有编程语言通用的格式，只能处理简单的数据类型
import json
f = open("test.txt", "r")
data = json.loads(f.read())
print(data["age"])
"""

# pickle是Python中独有的数据格式，可以支持任意数据类型。其他编程语言不支持pickle数据格式
import pickle
def test(name):
    print("name:", name)

f = open("test.txt", "rb")
data = pickle.load(f)  # 和data = pickle.loads(f.read())效果一样
print(data["func"]("Alex"))
