# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

"""
import time

def deco(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the fun run time is %s " % (stop_time - start_time))

def test1():
    time.sleep(3)
    print("in the test1")

def test2():
    time.sleep(3)
    print("in the test2")

deco(test1)
deco(test2)
"""

"""
import time

def timer(func):  # timer(test1) func=test1
    def deco():
        start_time = time.time()
        func()  # run test1
        stop_time = time.time()
        print("the fun run time is %s " % (stop_time - start_time))
    return deco

@timer  # test1 = timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")
@timer
def test2():
    time.sleep(3)
    print("in the test2")

# test1 = timer(test1)  # 返回deco函数的内存地址即deco
test1()  # 运行deco函数
test2()
# deco(test2)
"""

import time

def timer(func):  # timer(test1) func=test1
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)  # run test1
        stop_time = time.time()
        print("the fun run time is %s " % (stop_time - start_time))
    return deco

@timer  # test1 = timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")
@timer
def test2(name, age):
    time.sleep(3)
    print("in the test2：", name, age)

# test1 = timer(test1)  # 返回deco函数的内存地址即deco
test1()  # 运行deco函数
test2("Alex", 22)
# deco(test2)
