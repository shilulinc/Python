#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ShiLu
# Date:2017-08-20

# 用户输入密码时可以使用getpass模块进行密文输入，但在Pycharm中此模块无法使用，故用明文进行输入。

# 模拟登陆
# 1.用户输入账号密码进行登录
# 2.用户信息保存在文件中
# 3.用户名或者密码输错三次锁定退出

import sys  # 导入sys模块

file1 = open("lock.txt", "r+")  # 以读模式打开被锁定用户的文件，并可写
file1_list = file1.readlines()  # 读出被锁定用户文件的内容
file1.close()  # 关闭文件

file2 = open("users_info.txt", "r+")
file2_list = file2.readlines()
file2.close()

file3 = open("password.txt", "r+")
file3_list = file3.readlines()
file3.close()

lock_info = []  # 用来存放修改格式后的被锁定用户
user_info = []
password_info = []

for i in file1_list:  # 遍历被锁定用户文件
    line1 = i.strip("\n")  # 移除末尾的换行符，并用新的变量名进行引用
    lock_info.append(line1)  # 把新引用的变量追加到修改之后的锁定列表

for j in file2_list:
    line2 = j.strip("\n")
    user_info.append(line2)

for k in file3_list:
    line3 = k.strip("\n")
    password_info.append(line3)

user_name = input("请输入用户:")  # 使用input输入并赋值给username变量
if user_name in lock_info:  # 使用if判断用户输入的参数是否在已锁定列表中
    print("此用户为已锁定用户，请联系管理员！")
    sys.exit()  # sys模块的.exit()方法表示程序退出

if user_name in user_info:  # 使用if判断用户输入的参数是否在用户列表中
    user_passwd = input("请输入密码:")  # 使用input输入并赋值给user_passwd变量
    if user_passwd == password_info[0][-3:] and user_info[0] == password_info[0][:-4]:
    # 使用if判断输入密码是否等于密码列表中的后三位数并且输入用户是否等于密码表中的前三位数
        print("欢迎登陆！")
        sys.exit()
    else:
        count1 = 0  # 计数器count1从0开始计数
        while count1 < 3:  # 输入密码次数小于3次会不断循环
            print("密码不正确！")
            count1 += 1  # 密码输错后循环次数加1
            print("剩余可重试次数%s" % (3 - count1))  # 提醒用户剩余可重试次数
            if 3 - count1 == 0:  # 使用if判断，如果输错3次则跳出本次循环并锁定退出
                break
            user_passwd = input("请重新输入:")  # 重新输入，如果输入正确，则程序退出
            if user_passwd == password_info[0][-3:] and user_info[0] == password_info[0][:-4]:
                print("欢迎登陆")
                sys.exit()
        if 3 - count1 == 0:
            print("输错达到三次，已锁定！")
            sys.exit()

else:  # 如果输入的用户信息不在用户列表中，则执行以下代码，部分代码逻辑和以上相同，相当于代码复用
    count2 = 0  # 计数器count2从0开始计数
    while count2 < 3:  # 当计数器count2小于3时进行循环
        print("用户不存在")
        count2 += 1
        print("剩余可重试次数%s" % (3 - count2))
        if 3 - count2 == 0:
            break
        user_name = input("请重新输入:")
        if user_name in lock_info:
            print("此用户为已锁定用户，请联系管理员！")
            sys.exit()

        if user_name in user_info:
            user_passwd = input("请输入密码:")
            if user_passwd == password_info[0][-3:] and user_info[0] == password_info[0][:-4]:
                print("欢迎登陆！")
                sys.exit()
            else:
                count3 = 0  # 计数器count3从0开始计数
                while count3 < 3:  # 当计数器count3小于3时进行循环
                    print("密码不正确！")
                    count3 += 1
                    print("剩余可重试次数%s" % (3 - count3))
                    if 3 - count3 == 0:
                        break
                    user_passwd = input("请重新输入:")
                    if user_passwd == password_info[0][-3:] and user_info[0] == password_info[0][:-4]:
                        print("欢迎登陆！")
                        sys.exit()
                if 3 - count3 == 0:
                    print("输错达到三次，已锁定！")
                    sys.exit()

    if 3 - count2 == 0:
        print("输错达到三次，已锁定！")
        sys.exit()
