# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Shi Lu"

class Dog(object):

    def __init__(self,name): # 构造函数，构造方法 == 初始化方法
        self.NAME = name

    def sayhi(self): # 类的方法
        print("hello,I am a dog. my name is", self.NAME)

    def eat(self,food):
        print("%s is eating %s" %(self.NAME, food))

d=Dog("lichuang")
d2=Dog("chuang2")
d.sayhi()
d2.sayhi()
