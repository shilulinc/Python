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
import json
def test(name):
    print("name:", name)

f = open("test.txt", "r")
data =json.load(f)  # 和data = pickle.loads(f.read())效果一样
print(data["func"]("Alex"))

for line in f:
    print(json.loads(line))

# 说明：在Python2.x中可以dumps多次，也可以loads多次，但效果不好
# 在Python3.x中，只可以loads一次，只dumps一次，只loads一次，永远保证数据都是最新的
