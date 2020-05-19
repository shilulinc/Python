#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"


# def change_name():
#     global name
#     name = "alex"
# change_name()
# print(name)


school = "Old Boy"


def change_name(name):
    global school # 声明全局变量
    school = "Ma Ge"
    print("before change", name, school)
    name = "Alex Li" # 这个函数就是这个变量的作用域
    print("after name", name)


name = "alex"
change_name(name)
# print(name)
print("school:", school)


# names = ["Alex", "Jack", "Rain"]
# def change_name():
#     names[0] = "金角大王"
#     print("inside func:", names)
#
# change_name()
# print(names)
