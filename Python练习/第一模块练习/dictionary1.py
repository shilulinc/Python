# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

# 创建字典的方法

# 传统的文字表达法
a = {'name':'Allen','age':21,'gender':'male'}
print(a)

# 动态分配键值
b = {}
b['name']='Allen'
b['age']=21
b['gender']='male'
print(b)

# 字典键值表
c = dict(name='Allen', age=14, gender='male')
print(c)

# 字典键值元组表
d = dict([('name','Allen'),('age',21),('gender','male')])
print(d)

# 所有键的值都相同或者赋予初始值
e = dict.fromkeys(['height','weight'],'normal')
print(e)
