# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

"""
import time
def bar():
    time.sleep(3)
    print("in the bar")

def test1(func):
    start_time = time.time()
    func()  # run bar
    stop_time = time.time()
    print("the func run time is %s" % (stop_time - start_time))
test1(bar)
"""

import time
def bar():
    time.sleep(3)
    print("in the bar")

def test2(func):
    print(func)
    return func

bar = test2(bar)
bar()
