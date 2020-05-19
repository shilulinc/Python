# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

"""
# json是所有编程语言通用的格式，只能处理简单的数据类型
import json
info = {
    "name":"alex",
    "age":22
}
"""

def test(name):
    print("name:", name)
info = {
    "name":"Alex",
    "age":22,
    "func":test
}
# pickle是Python中独有的数据格式，可以支持任意数据类型。其他编程语言不支持pickle数据格式
import pickle
f = open("test.txt", "wb")
# print(pickle.dumps(info))
pickle.dump(info, f)  # 和f.write(pickle.dumps(info))效果一样
# f.write(str(info))
f.close()
