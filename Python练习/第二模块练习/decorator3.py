# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

"""
# 函数的嵌套
def foo():
    print("in the foo")
    def bar():
        print("in the bar")
    bar()
foo()
"""

x = 0
def grandpa():
    x = 1
    def dad():
        x = 2
        def son():
            x = 3
            print(x)
        son()
    dad()
grandpa()
