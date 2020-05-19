# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ShiLU

"""
f2 = []
f1 = open("password.txt", "r+")
f1_read = f1.readlines()
for i in f1_read:
    j = i.strip("\n")
    f2.append(j)
print(f2[0][:-4])
f1.close()
"""

"""
a, b = 2, 1 ;c = a if b > a else None
print(c)
"""

"""
a = 2
b = a
a = 3
print(b)
"""

"""
a = lambda x:x**2
print(a(3))
"""

"""
d1 = {"k1": "value1"}

if "k1" in d1:
    print(d1["k1"])
else:
    print("not found")

print(d1.setdefault("k2", "value2"))
print(d1)
print(d1.setdefault("k2", "value3"))
print(d1)
d1.setdefault("k3", [])
print('一级菜单'.center(40, '-'))
print(d1.keys())
print(d1)
dict = dict(name="allen", age="40")
print(dict)
"""

"""
import sys
print(sys.path)
print(sys.argv)
"""
