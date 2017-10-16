# _*_ coding:utf-8 _*_
# Author:ShiLu
# Date:2017-10-17

# 一级菜单


def menu1():
    print('一级菜单'.center(40, '-'))  # 打印分界线
    for index1,key1 in enumerate(dic.keys(), 1):  # 遍历一级菜单
        print(index1, key1)
        dic_key[str(index1)] = key1  # 生成一级菜单字典
    print(dic_key)
    choose = input("请选择1级菜单，输入B返回上一级菜单，输入Q退出菜单:")  # 为一级菜单输入定义变量choose1
    if choose == 'Q':
        quit()
    elif choose == 'B':
        print("此处为一级菜单，不能返回")
    elif dic_key.get(choose):  # 字典取值
         menu2(dic_key[choose])  # 将二级菜单的key传给函数menu2
    else:
        print("输入有误，请重新输入")

# 二级菜单


def menu2(choose1):
    print('二级菜单'.center(40, '-'))
    for index2,key2 in enumerate(dic[choose1].keys(), 1):  # 遍历二级菜单
        print(index2, key2)
        dic_key[str(index2)] = key2  # 生成二级菜单字典
    print(dic_key)
    choose2 = input("请选择2级菜单，输入B返回上一级菜单，输入Q退出菜单")  # 为二级菜单输入定义变量choose2
    if choose2 == 'Q':
        quit()
    elif choose2 == 'B':
        menu1()
    elif dic_key.get(choose2):
        menu3(choose1, dic_key[choose2])
    else:
        print("输入有误，请重新输入")

# 三级菜单


def menu3(choose1, choose2):
    print('三级菜单'.center(40, '-'))
    for index3, key3 in enumerate(dic[choose1][choose2].keys(), 1):
        print(index3, key3)
        dic_key[str(index3)] = key3
    print(dic_key)
    choose3 = input("请选择3级菜单，输入B返回上一级菜单，输入Q退出菜单")
    if choose3 == 'Q':
        quit()
    elif choose3 == 'B':
        menu2(choose1)
    elif dic_key.get(choose3):
        menu4(choose1, choose2, dic_key[choose3])
    else:
        print("输入有误，请重新输入")


def menu4(choose1, choose2, choose3):
    for index4, key4 in enumerate(dic[choose1][choose2][choose3], 1):
        print(index4, key4)


if __name__ == '__main__':
    dic = {
            '华北': {
                '北京':
                    {
                        '海淀': ['中关村', '青龙桥'],
                        '昌平': ['回龙观', '沙河']
                    },
                '河北':
                    {
                        '石家庄': ['新华', '桥西'],
                        '保定': ['竞秀', '莲池']
                    }
            },
            '华东': {
                '上海':
                    {
                        '浦东新区': ['潍坊新村', '陆家嘴'],
                        '黄浦区': ['南京东路', '外滩']
                    },
                '浙江':
                    {
                        '杭州': ['上城', '下城'],
                        '宁波': ['海曙', '江北']
                    }
            }
         }
    dic_key = {}
    while True:
        menu1()
