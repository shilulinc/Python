#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

# return的作用：1.返回值 2.return之后的程序不再执行
def test1():
    """testing1"""
    print("in the test1")

def test2():
    """testing2"""
    print("in the test2")
    return 0

def test3():
    """testing3"""
    print("in the test3")
    return 1, "Alex", ["Alex", "Wusir"], {"name": "Alex"}

x = test1()
y = test2()
z = test3()
print(x)
print(y)
print(z)
