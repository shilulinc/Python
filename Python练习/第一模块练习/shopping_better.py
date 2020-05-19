#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

"""
f_list = []
f = open("goods_info", "r+", encoding="utf-8")
for i in f:
    f_list.append(i.strip("\n").split(":"))
# print(f_list)
f_list_new = []
for i in f_list:
    f_list_new.append([i[0], int(i[1])])
f_list = f_list_new
print(f_list)
"""

"""
file = open("goods_info", "r+", encoding="utf-8")

# name = input("请输入用户名：")
# passwd = input("请输入密码：")

list = []
for i in file:
    list.append(i.strip("\n"))
print(list)
new_list = str(list)
d = eval(new_list)
"""

user_dic = {} # 用户信息文件转换成字典
with open("user_info", "r+", encoding="utf-8") as user_fd:
    for i in user_fd:
        (key, value) = i.strip("\n").split(":", 1)
        user_dic[key] = value
# print(user_dic)

name = input("请输入用户名：")
passwd = input("请输入密码：")
while True:
    if name in user_dic: # 如果用户在已有的用户信息文件中
        if str(passwd) in user_dic[name]:
            salary =  eval(user_dic[name])[passwd]
            print(type(salary))
            print("\033[32;1m欢迎%s登陆！，当前薪水为%s!\033[0m" % (name, salary))
            break
        else:
            passwd = input("密码输入错误，请重新输入:")
            continue
    else: # 判断为首次登陆，将用户名，密码，薪水存入字典中
        passwd_salary = {}
        salary_new = input("欢迎首次登陆，请输入薪水：")
        passwd_salary[passwd] = int(salary_new)
        user_dic[name] = str(passwd_salary)
        with open("user_info", "a+", encoding="utf-8") as user_fd:
            user_fd.write("%s:%s" % (name, str(passwd_salary)) + "\n")
        break

# 用户信息文件转换为字典
with open("user_info", "r+", encoding="utf-8") as user_fd:
    for i in user_fd:
        (key, value) = i.strip("\n").split(":", 1)
        user_dic[key] = value

goods_dic = {} # 把商品信息文件转换为字典
with open("goods_info", "r+", encoding="utf-8") as goods_fd:
    for i in goods_fd:
        (key, value) = i.strip("\n").split(":")
        goods_dic[key] = int(value)
goods_list = [] # 把商品信息字典转换为列表
for i in goods_dic.items():
    goods_list.append(tuple(i))

shopping_new = []
salary1 =  eval(user_dic[name])[passwd]
while True:
    for index, item in enumerate(goods_list, 1): # 枚举商品信息
        print(index, item)
    user_choice = input("请根据编号选择商品，输入C查询已购商品信息，输入Q退出！")
    if name not in user_dic:
        print("首次登陆，购物信息为空！")
    else:
        if user_choice == "C" and name in user_dic:
            shopping_info_dic = {}
            with open("shopping_info", "r+", encoding="utf-8") as shopping_info_fd:
                for i in shopping_info_fd:
                    (key, value) = i.strip("\n").split(":", 1)
                    shopping_info_dic[key] = value
            print("已购商品信息如下：%s" % shopping_info_dic)
            user_choice = input("继续购物请输入Y：")
            if user_choice == "Y":
                if user_choice.isdigit():
                    user_choice = int(user_choice)
                    if user_choice < len(goods_list) + 1 and user_choice >= 1:
                        goods_item  = goods_list[user_choice - 1]
                        shopping_new.append(goods_item)
                        salary1 -= int(goods_item[1])
                        print(salary1)
                        if int(goods_item[1]) < salary1: # 买得起
                            print("你选择的商品\033[31;1m%s\033[0m已加入购物车！余额还剩\033[32;1m%s\033[0m!" \
                                  % (goods_item, salary1))
                            # print("购物车信息如下：%s" % shopping_new)
                        else:
                            print("余额不足，已退出！")
                            exit()
                    else:
                        print("你选择的商品不存在，请重新选择！")
        elif user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice < len(goods_list) + 1 and user_choice >= 1:
                    goods_item  = goods_list[user_choice - 1]
                    shopping_new.append(goods_item)
                    salary1 -= int(goods_item[1])
                    print(salary1)
                    if int(goods_item[1]) < salary1: # 买得起
                        print("你选择的商品\033[31;1m%s\033[0m已加入购物车！余额还剩\033[32;1m%s\033[0m!" \
                              % (goods_item,salary1))
                        print("购物车信息如下：%s" % shopping_new)
                        # shopping_all = dict(shopping_info_dic, **eval())
                    else:
                        print("余额不足，已退出！")
                        exit()
                else:
                    print("你选择的商品不存在，请重新选择！")
        elif user_choice == "Q":
            shopping_info_dic = {}
            with open("shopping_info", "r+", encoding="utf-8") as shopping_info_fd:
                for i in shopping_info_fd:
                    (key, value) = i.strip("\n").split(":", 1)
                    shopping_info_dic[key] = value
            shopping_info_list = list(eval(shopping_info_dic[name]).items()) # 已购商品列表
            shopping_all = shopping_info_list + shopping_new
            print("用户%s购物车信息如下shopping_all：%s" % (name, shopping_all))
            exit()
        else:
            print("输入错误，请重新输入商品编号！")
