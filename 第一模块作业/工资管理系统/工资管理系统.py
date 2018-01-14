# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

# 此为实现员工工资管理的简易程序
# 可以实现查询、修改、增加、退出功能
# 可以实现多层循环

items_list = ["查询员工工资", "修改员工工资", "增加新员工记录", "退出"]

# 把员工工资信息文件转换成字典
info_dic = {}
with open("info", "r", encoding="utf-8") as info_fd:
    for i in info_fd:
        (key, value) = i.strip("\n").split(" ")
        info_dic[key] = int(value)

while True:  # 开始循环
    for index, item in enumerate(items_list, 1):  # 枚举列表
        print(index, item)
    choice = input("请根据编号输入：")

    # 进入多条件判断
    if choice == "1":
        user_query = input("请输入要查询的员工姓名：")
        if user_query in info_dic.keys():
            print("%s的工资是：%s" % (user_query, info_dic[user_query]))

    elif choice == "2":
        user_change = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：")
        d1 = {}
        with open("info", "r", encoding="utf-8") as info_fd:
            for i in info_fd:
                (key, value) = user_change.strip("\n").split(" ")
                d1[key] = int(value)

        # 重新生成新的员工工资信息文件
        file_data = ""
        with open("info", "r", encoding="utf-8") as info_fd:
            for line in info_fd:
                if list(d1)[0] in line:
                    line = line.replace(str(info_dic[list(d1)[0]]), str(d1[list(d1)[0]]))
                file_data += line
        with open("info", "w", encoding="utf-8") as info_fd:
            info_fd.write(file_data)
        print("修改成功！")

        info_dic2 = {}
        with open("info", "r", encoding="utf-8") as info_fd2:
            for i in info_fd2:
                (key, value) = i.strip("\n").split(" ")
                info_dic2[key] = int(value)

        while True:
            for index, item in enumerate(items_list, 1):
                print(index, item)
            choice = input("请根据编号输入：")
            if choice == "1":
                user_query = input("请输入要查询的员工姓名：")
                if user_query in info_dic.keys():
                    print("%s的工资是：%s" % (user_query, info_dic2[user_query]))
                    break
            else:
                print("输入无效！请重新输入！")

    elif choice == "3":
        user_add = input("请输入要增加的员工姓名和工资，共空格分割（例如：Eric 100000）：")
        with open("info", "a+", encoding="utf-8") as info_fd:
            info_fd.write(user_add + "\n")
        print("增加成功！")

        info_dic3 = {}
        with open("info", "r", encoding="utf-8") as info_fd3:
            for i in info_fd3:
                (key, value) = i.strip("\n").split(" ")
                info_dic3[key] = value

        while True:
            for (index, item) in enumerate(items_list, 1):
                print(index, item)
            choice = input("请根据编号输入：")

            if choice == "1":
                user_query = input("请输入要查询的员工姓名：")
                print("%s的工资是：%s" % (user_query, info_dic3[user_query]))
                break

            elif choice == "2":
                user_change = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：")
                d2 = {}
                with open("info", "r", encoding="utf-8") as info_fd:
                    for i in info_fd:
                        (key, value) = user_change.strip("\n").split(" ")
                        d2[key] = int(value)

                file_data2 = ""
                with open("info", "r", encoding="utf-8") as info_fd:
                    for line in info_fd:
                        if list(d2)[0] in line:
                            line = line.replace(str(info_dic3[list(d2)[0]]), str(d2[list(d2)[0]]))
                        file_data2 += line
                with open("info", "w", encoding="utf-8") as info_fd:
                    info_fd.write(file_data2)
                print("修改成功！")

                info_dic4 = {}
                with open("info", "r", encoding="utf-8") as info_fd4:
                    for i in info_fd4:
                        (key, value) = i.strip("\n").split(" ")
                        info_dic4[key] = value

                while True:
                    for index, item in enumerate(items_list, 1):
                        print(index, item)
                    choice = input("请根据编号输入：")
                    if choice == "1":
                        user_query = input("请输入要查询的员工工资：")
                        if user_query in info_dic4.keys():
                            print("%s的工资是%s！" % (user_query, info_dic4[user_query]))
                            break
                    else:
                        print("输入无效！请重新输入！")

            elif choice == "3":
                user_add = input("请输入要增加的员工姓名和工资，共空格分割（例如：Eric 100000）：")
                with open("info", "a+", encoding="utf-8") as info_fd5:
                    info_fd5.write(user_add + "\n")
                print("增加成功！")

            elif choice == "4":
                print("再见！")
                exit()

    elif choice == "4":
        print("再见！")
        exit()

    else:
         print("输入错误！请重新输入！")
