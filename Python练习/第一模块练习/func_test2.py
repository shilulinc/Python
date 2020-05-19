#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

import time

def logger():
    time_formate = "%Y-%m-%d %X"
    current_time = time.strftime(time_formate)
    with open("a.txt", "a+") as f:
        f.write("%s end action\n" % current_time)

def test1():
    """testing1"""
    print("in the test1")
    logger()

def test2():
    """testing2"""
    print("in the test2")
    logger()

def test3():
    """testing3"""
    print("in the test3")
    logger()

test1()
test2()
test3()
