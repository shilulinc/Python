# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

"""
a = {"x": 1}
print(a)
print(type(a))

name = input("请输入：")
shopping_info_dic = {}
with open("shopping_info", "r+", encoding="utf-8") as shopping_info_fd:
    for i in shopping_info_fd:
        (key2, value2) = i.strip("\n").split(":", 1)
        shopping_info_dic[key2] = value2
print(dict(shopping_info_dic[name]))
print(type(shopping_info_dic[name]))
"""
d = {"a": 1, "b": 2}
print(d)
print(list(d))
print(list(d)[0])

print(type(tuple(d)[0]))

print(d["a"])
print(str(list(d)[0]))