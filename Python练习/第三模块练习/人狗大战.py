# /usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Shi Lu"

def person(name,age,sex,job):
    data = {
        'name':name,
        'age':age,
        'sex':sex,
        'job':job
    }

    return data

def dog(name,dog_type):
    data = {
        'name':name,
        'type':dog_type
    }
    return data

d1 = dog("李磊","京巴")

p1 = person("严帅",36,"F","运维")

p2 = person("林海峰",27,"F","Teacher")

def bark(d):
    print("dog %s:wang.wang..wang..."%d['name'])


def walk(p):
    print("person %s is walking..." %p['name'])<br><br>

d1 = dog("李磊","京巴")
p1 = person("严帅",36,"F","运维")
p2 = person("林海峰",27,"F","Teacher")

walk(p1) bark(d1)
