#/usr/bin/env python
#_*_ coding:utf-8 _*_
__Author__ = "Shi Lu"

names = ["4Zhang Yang", "#!Gu Yun", "xXiang Peng", ["alex", "jack"], "Chen Ronghua", "Xu Liangchen"]

# for i in names: # 列表循环
#     print(i)

# range(1,10,2) # 步进取值
# print(names[0:-1:2]) # 步进打印 0表示开始 -1表示结束
# print(names[::2]) # 开始和结束的数字可以省略
print(names[:]) # 打印列表全部值

# names.append("Lei Haidong")
# names.insert(1, "Chen Ronghua")
# names.insert(3, "Xin Zhiyu")
# names[2] = "Xie Di"
# print(names)
# print(names[0], names[3])
# print(names[1:3]) # 切片 顾首不顾尾
# print(names[3]) # 切片
# print(names[-2:]) # 切片 取最后两个值，从左向右
# print(names[0:3]) # 切片 取最前三个值，从左向右
# print(names[:3]) # 切片 开始是0可以省略不写，和取最后的值一样

# Delete
# names.remove("Chen Ronghua") # 指定对象
# del names[1] # 指定索引
# names.pop(1) # 不加索引，默认删除最后一个对象；加索引，删除指定对象
# print(names)
# print(names.index("Xie Di")) # 打印指定对象的索引
# print(names[names.index("Xie Di")]) # 取值
# print(names.count("Chen Ronghua")) # 打印指定对象出现的次数
# names.clear() # 清空列表
# names.reverse() # 反转列表
# names.sort() # 按照ISCII顺序排列
# name2 = ["1", "2", "3", "4"]
# names.extend(name2)
# # del name2 # 删除变量
# print(names, name2)

# import copy
# name2 = names.copy() # 浅copy，只copy第一层
# name2 = copy.copy(names) # 同上
# name2 = copy.deepcopy(names) # 深copy，完全copy
# print(names)
# print(name2)

# names[2] = "向鹏"
# names[3][0] = "ALEXANDER" # 修改列表中索引为3的第一个值为ALEXANDER
# print(names)
# print(name2)

# 补充:
import copy
person = ["name", ["saving", 100]]

p1 = copy.copy(person)
# # p2 = person[:]
# # p3 = list(person)

# p1 = person[:]
p2 = person[:]
# p1[0] = "alex"
p2[0] = "fengjie"
p1[1][1] = 50
print(p1)
print(p2)
