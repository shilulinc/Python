#/usr/bin/env python
#_*_ coding:utf-8 _*_
__Author__ = "Shi Lu"

list_1 = ["1", "2", "3", "4", "5", "4", "5", "8"]
list_1 = set(list_1)
# print(list_1, type(list_1))

list_2 = set(["2", "3", "5", "6", "7", "10"])
# print(list_1, list_2)


list_3 = set(["1", "3", "5"])
list_4 = set(["2", "4", "6"])
print(list_1.intersection(list_2)) # 求交集
print(list_1.union(list_2)) # 求并集
print(list_1.difference(list_2)) # 求差集 in list_1 but not in list_2
print(list_2.difference(list_1)) # 求差集 in list_2 but not in list_1
print(list_1.issubset(list_2)) # 判断list_1是否list_2的子集
print(list_1.issuperset(list_2)) # 判断list_1是否list_2的父集
print(list_3.issubset(list_1)) # 判断list_3是否list_1的子集
print(list_1.issuperset(list_3)) #判断list_1是否list_3的父集
print(list_1.symmetric_difference(list_2)) # 求对称差集 项在list_1或list_2中，但不同时在两者中
print(list_3.isdisjoint(list_4)) # 判断如果list_3和list_4没有交集，返回True，否则，返回False


print(list_1 & list_2) # 求交集
print(list_1 | list_2) # 求并集
print(list_1 - list_2) # 求差集 in list_1 but not in list_2
print(list_1 ^ list_2) # 求对称差集 元素在list_1或list_2中，但不同时在两者中

list_1.add("111")
list_1.add("112")

print(list_1)
list_1.update(["333", "555", "777"])
print(list_1)
print(list_1.pop()) # 删除任意一个元素
#list_1.remove("aaa") # 删除指定的一个元素，如果没有则会报错
#list_1.discard("aaa") # 删除指定的一个元素，如果没有不会报错
