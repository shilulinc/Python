#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

# 当实参数目不固定时使用此方式，接受N个位置参数转换成元组
# def test(*args):
#     """testing"""
#     print(args)
#
#
# test(1,2,3,4,5)

# def test1(x,*args):
#     """testing1"""
#     print(x)
#     print(args)
#
#
#test1(1,2,3,4,5)
# test1(*[1,2,3,4,5]) args=tuple([1,2,3,4,5])

# 把N个关键字参数转换成字典的方式
# def test2(**kwargs):
#     """testing2"""
#     print(kwargs)
#     print(kwargs["name"])
#     print(kwargs["age"])
#
#
# test2(name="Alex", age=8)
# test2(**{"name":"Alex", "age":8})

# 位置参数不能放在关键字参数后面
# def test3(name,**kwargs):
#     """testing3"""
#     print(name)
#     print(kwargs)
#
#
# test3("Alex", age=8, sex="m")

'''
def test4(name,age=18,**kwargs):
    """testing4"""
    print(name)
    print(age)
    print(kwargs)


test4("Alex", age=34, sex="m", hobby="tesla")
'''


def test5(name, age=18, *args, **kwargs):
    """testing5"""
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST5")


def logger(source):
    """testing"""
    print("from %s" % source)


test5("Alex", age=34, sex="m", hobby="tesla")
