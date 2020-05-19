#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

# f = open("yesterday", "r", encoding="utf-8")
with open("yesterday", "r", encoding="utf-8") as f, \
    open("yesterday2", "r", encoding="utf-8") as f2:

    for line in f:
         print(line.strip("\n"))
