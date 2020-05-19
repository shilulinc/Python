#/usr/bin/env python
#_*_ coding:utf-8 _*_
__Author__ = "Shi Lu"

d = {
    "北京": {
        "朝阳": {
            "望京": ["奔驰", "陌陌"],
            "国贸": ["CICC", "HP"]
        },
        "昌平": {
            "沙河": ["oldboy", "test"],
            "天通苑": ["链家地产", "我爱我家"]
        }
    },
    "上海": {
        "闵行": {
            "人民广场": {
                "炸鸡店": {

                }
            }
        },
        "闸北": {
            "火车站": {
                "携程": {

                }
            }
        }
    }
}
print(d)

while True:
    for i in d:
        print(i)

    choice = input("请进入1>>:")
    if choice in d: # 如果输入的内容在字典里，则进入下一层
        while True: # 进入下一层循环完成之后，等待用户输入"choice1"
            for i2 in d[choice]:
                print("\t", i2)
            choice2 = input("请进入2>>:")
            if choice2 in d[choice]:
                while True:
                    for i3 in d[choice][choice2]:
                        print("\t\t", i3)
                    choice3 = input("请进入3>>:")
                    if choice3 in d[choice][choice2]:
                        for i4 in d[choice][choice2][choice3]:
                            print("\t\t\t",i4)
                        choice4 = input("最后一层，按B返回>>:")
                        if choice4 == "B":
                            pass # 占位符，什么也不做
                    if choice3 == "B":
                        break
            if choice2 == "B":
                break
