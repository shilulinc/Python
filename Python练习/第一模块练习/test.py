#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Yorick"

dic = \
    {

        '北京': {

            '东城':

                {

                    '沙河': ['老男孩', '恋家'],


                },


        },

        '上海': {

            '虹桥':

                {

                    '虹桥机场': ['超市', '特产店'],

                },


        }

    }

print(dic)
dic_key = {}
for index, key in enumerate(dic.keys(),1):
    print(index, key)
    dic_key[str(index)] = key
print(dic_key)

"""
choose = input("请选择1级菜单，输入B返回上一级菜单，输入Q退出菜单:")
if dic_key.get(choose):
    menu2(dic_key[choose])      # 将二级菜单的key传给函数menu2
else:
    print("输入有误，请重新输入")
"""

print(dic_key.get(index))


