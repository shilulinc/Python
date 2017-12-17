# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"


def goods_list_func():
    """定义函数，枚举商品信息"""

    # 把商品信息文件转换为字典
    goods_dic1 = {}
    with open("goods_info", "r+", encoding="utf-8") as goods_fd1:
        for i in goods_fd1:
            (key1, value1) = i.strip("\n").split(":")
            goods_dic1[key1] = int(value1)

    # 把商品信息字典转换为列表
    goods_list1 = []
    for i in goods_dic1.items():
        goods_list1.append(tuple(i))

    # 枚举商品信息
    for index1, item1 in enumerate(goods_list1, 1):
        print(index1, item1)


choice = input("请根据用户或商家编号选择不同的入口，输入U进入用户入口，输入M进入商家入口：") # 根据不同的输入进入不同的程序
if choice == "U":  # 如果输入U进入用户入口
    print("欢迎进入用户入口！")
    users_dic = {}  # 用户信息文件转换成字典
    with open("users_info", "r+", encoding="utf-8") as users_fd2:
        for i in users_fd2:
            (key2, value2) = i.strip("\n").split(":", 1)
            users_dic[key2] = value2
    name = input("请输入用户名：")
    passwd = input("请输入密码：")
    while True:
        if name in users_dic:  # 如果用户在已有的用户信息文件中
            if passwd in users_dic[name]:
                salary = eval(users_dic[name])[passwd]
                print("\033[32;1m欢迎%s登陆！，当前薪水为%s!\033[0m" % (name, salary))
                break
            else:
                passwd = input("密码输入错误，请重新输入:")
                continue
        else:  # 否则为首次登陆，将用户名、密码、薪水存入字典并写入到用户信息文件中
            passwd_salary = {}
            salary_new = input("欢迎首次登陆，请输入薪水：")
            passwd_salary[passwd] = int(salary_new)
            users_dic[name] = str(passwd_salary)
            with open("users_info", "a+", encoding="utf-8") as users_fd2:
                users_fd2.write("%s:%s" % (name, str(passwd_salary)) + "\n")
            break

    # 把商品信息文件转换为字典
    goods_dic2 = {}
    with open("goods_info", "r+", encoding="utf-8") as goods_fd2:
        for i in goods_fd2:
            (key2, value2) = i.strip("\n").split(":")
            goods_dic2[key2] = int(value2)

    # 把商品信息字典转换为列表
    goods_list2 = []
    for i in goods_dic2.items():
        goods_list2.append(tuple(i))

    # 定义新购物信息字典
    shopping_new = []
    salary1 = eval(users_dic[name])[passwd]

    while True:
        goods_list_func()  # 调用函数，生成商品信息

        def users_balance_func1():
            """定义用户购物后剩余薪水函数"""
            file_data1 = ""
            with open("users_info", "r", encoding="utf-8") as users_fd3:
                for line in users_fd3:
                    if str(eval(users_dic[name])[passwd]) in line:
                        line = line.replace(str(eval(users_dic[name])[passwd]), str(salary1))
                    file_data1 += line
            with open("users_info", "w", encoding="utf-8") as users_fd3:
                users_fd3.write(file_data1)

        user_choice = input("请根据编号选择商品，输入C查询已购商品信息，输入Q退出：")
        names_list = ["Tom", "Jack", "Rain"]  # 以列表形式列出已有的用户信息
        if user_choice == "C":  # 如果查询已购商品信息
            if name not in names_list:
                print("首次登陆，购物信息为空！")
            else:
                shopping_info_dic = {}
                with open("shopping_info", "r+", encoding="utf-8") as shopping_info_fd:
                    for i in shopping_info_fd:
                        (key2, value2) = i.strip("\n").split(":", 1)
                        shopping_info_dic[key2] = value2
                print("\033[32;1m已购商品信息如下：%s\033[0m" % shopping_info_dic[name])
                user_choice = input("继续购物请输入Y，输入Q退出：")
                if user_choice == "Y":
                    salary2 =  eval(users_dic[name])[passwd]

                    def users_balance_func2():
                        """定义用户购物后剩余薪水函数"""
                        file_data2 = ""
                        with open("users_info", "r", encoding="utf-8") as users_fd3:
                            for line in users_fd3:
                                if str(eval(users_dic[name])[passwd]) in line:
                                    line = line.replace(str(eval(users_dic[name])[passwd]), str(salary2))
                                file_data2 += line
                        with open("users_info", "w", encoding="utf-8") as users_fd3:
                            users_fd3.write(file_data2)

                    while True:
                        goods_list_func()  # 调用函数，生成商品信息
                        user_choice = input("请根据编号选择商品，输入Q退出：")
                        if user_choice.isdigit():  # 如果用户输入数字
                            user_choice = int(user_choice)
                            if user_choice < len(goods_list2) + 1 and user_choice >= 1:  # 如果用户输入的数字在商品编号中
                                goods_item = goods_list2[user_choice - 1]
                                shopping_new.append(goods_item)
                                salary2 -= int(goods_item[1])
                                if int(goods_item[1]) < salary2:  # 如果用户买得起
                                    print("你选择的商品\033[31;1m%s\033[0m已加入购物车！余额还剩\033[32;1m%s\033[0m!" \
                                          % (goods_item, salary2))
                                    print("\033[32;1m新购商品信息如下：%s\033[0m" % shopping_new)
                                else:
                                    print("余额还剩%s，余额不足，已退出！" % salary2)
                                    users_balance_func2()  # 调用用户购物后剩余薪水函数2
                                    exit()
                            else:
                                print("你选择的商品不存在，请重新选择！")
                        elif user_choice == "Q":  # 如果用户输入Q退出
                            shopping_info_list = list(eval(shopping_info_dic[name]).items())  # 已购商品列表
                            shopping_all = shopping_info_list + shopping_new
                            print("\033[32;1m用户%s购物车信息如下，shopping_all：%s\033[0m" % (name, shopping_all))
                            users_balance_func2()  # 调用用户购物后剩余薪水函数2
                            exit()
                        else:
                            user_choice = input("输入错误，请重新输入：")
                elif user_choice == "Q":  # 如果用户输入Q退出
                    exit()
                else:
                    user_choice =input("输入错误，请继续：")
        elif user_choice.isdigit():  # 如果用户输入的内容为数字
                user_choice = int(user_choice)
                if user_choice < len(goods_list2) + 1 and user_choice >= 1:  # 如果用户输入的数字在商品编号中
                    goods_item  = goods_list2[user_choice - 1]
                    shopping_new.append(goods_item)
                    salary1 -= int(goods_item[1])
                    if int(goods_item[1]) < salary1:  # 如果用户买得起
                        print("你选择的商品\033[31;1m%s\033[0m已加入购物车！余额还剩\033[32;1m%s\033[0m!" \
                              % (goods_item, salary1))
                        print("购物车信息如下：%s" % shopping_new)
                    else:
                        print("余额还剩%s，余额不足，已退出！" % salary1)
                        print("购物车信息如下：%s" % shopping_new)
                        users_balance_func1()  # 调用用户购物后剩余薪水函数1
                        exit()
                else:
                    print("你选择的商品不存在，请重新选择！")
        elif user_choice == "Q":  # 如果用户输入Q，打印已购商品信息和新购商品信息的汇总
            shopping_info_dic = {}
            with open("shopping_info", "r+", encoding="utf-8") as shopping_info_fd:
                for i in shopping_info_fd:
                    (key2, value2) = i.strip("\n").split(":", 1)
                    shopping_info_dic[key2] = value2
            l_name = ["Tom", "Jack", "Rain"]
            if name not in l_name:  # 如果输入name在已有的用户列表中
                shopping_all = shopping_new
            else:
                shopping_info_list = list(eval(shopping_info_dic[name]).items())  # 已购商品列表
                print(shopping_info_list)
                shopping_all = shopping_info_list + shopping_new
            print("\033[32;1m用户%s购物车信息如下，shopping_all：%s\033[0m" % (name, shopping_all))
            users_balance_func1()  # 调用用户购物后剩余薪水函数1
            exit()
        else:
            print("输入错误，请重新输入商品编号！")
elif choice == "M":  # 如果输入M进入商家入口
    print("欢迎进入商家入口！")
    while True:
        goods_list_func()  # 调用函数，生成商品信息
        merchant_choice = input("输入A添加商品，输入C修改商品价格，输入Q退出：")
        if merchant_choice == "A":  # 如果输入A增加商品
            goods_add = input("请根据示例%s添加商品：" % "apple:10")
            with open("goods_info", "a+", encoding="utf-8") as goods_fd:
                goods_fd.write(goods_add + "\n")
        elif merchant_choice == "C":  # 如果输入C进入修改商品价格信息子程序
            item_old = input("请根据示例%s输入商品价格信息：" % "apple:10")
            item_new = input("请根据示例%s输入商品新价格信息：" % "apple:20")
            # 修改商品价格信息
            file_data3 = ""
            with open("goods_info", "r+", encoding="utf-8") as goods_fd:
                for line in goods_fd:
                    if item_old in line:
                        line = line.replace(item_old, item_new)
                    file_data3 += line
            with open("goods_info", "w", encoding="utf-8") as goods_fd:
                goods_fd.write(file_data3)
        elif merchant_choice == "Q":  # 如果输入Q退出
            exit()
        else:
            print("输入错误，请重新输入！")
