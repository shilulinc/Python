#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

# 把一个函数当作参数传递给另一个函数，另一个函数返回时会用到这个函数
def add(x, y, f):
    return f(x)+f(y)


res = add(3,-6,abs)

print(res)
