#/usr/bin/env python
#_*_ coding:utf-8 _*_
__Author__ = "Shi Lu"

# 已有的用户信息

product_list = [("iphone", 6000), ("ipad", 2000), ("bike", 1000), ("watch", 200), ("pc", 5000)]
shopping_list = []
salary = input("请输入工资：")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list, 1):
            print(index, item)
        user_choice = input("请选择商品：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) + 1 and user_choice >= 0:
                product_item = product_list[user_choice - 1]
                shopping_list.append(product_item)
                salary -= product_item[1]
                if product_item[1] < salary: # 买得起
                    print("你选择的商品 %s 已加入购物车，你的余额还剩 \033[31;1m%s\033[0m !" % (product_item, salary))
                else:
                    print("你的余额还剩 %s ，余额不足，已退出！" % salary)
                    exit()
            else:
                print("你选择的商品不存在，请重新选择！")
        elif user_choice == "Q":
            print("----shopping_info----")
            for i in shopping_list:
                print(i)
            exit()
        else:
            print("无效的输入！")
else:
    print("无效的输入！")
