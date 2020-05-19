# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

# 存储和读取序列化数据
"""
# 生成一个文件
import shelve
import datetime
d = shelve.open("shelve_test")  # 打开一个文件
name = ["Alex", "Rain", "Eric"]
info = {"age":22, "job":"it"}
d["name"] = name  # 持久化列表
d["info"] = info  # 持久化字典
d["date"] = datetime.datetime.now()
d.close()
"""

"""
# 读取一个文件
import shelve
import datetime
d = shelve.open("shelve_test")
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))
"""
