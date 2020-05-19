#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

"""
data = open("yesterday", encoding="utf-8").read()
print(data)
print()
"""


f = open("yesterday", encoding="utf-8") # 文件句柄
data = f.read()
print(data)
print("----data----")
data = f.read()
print("----data----")

"""
f = open("yesterday2", "w", encoding="utf-8") # 如果文件没有，会创建文件，并写进内容
f = open("yesterday3", "a", encoding="utf-8") # 如果文件没有，会创建文件，并追加内容
f.write("我爱北京天安门\n")
f.write("天安门上太阳升")

f = open("yesterday", "r", encoding="utf-8")

for i in range(5): # 读取前五行
    print(f.readline()) # 读取每一行

for line in f.readlines(): # f.readlines读取每一行加换行符，然后组成一个大列表
    print(line.strip()) # line.strip()去除换行符
"""

"""
low
for index, line in enumerate(f.readlines()): # 枚举
    if index == 9:
        print("----分隔符----")
        continue
    print(line.strip())

high
count = 0
for line in f: # 迭代器
    if count == 9:
        print("----分隔符----")
        count +=1
        continue
    print(line.strip())
    count +=1
"""

"""
f = open("yesterday", "r", encoding="utf-8")
print(f.tell()) # 打印指针位置
print(f.read(5))
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(0) # 指针指向起点
print(f.tell())
print(f.readline())
f.seek(10) # 指针指到第10个字符串
print(f.readline())
print(f.encoding) # 打印文件编码
print(f.fileno()) # 打印系统打开文件的编号
print(f.seekable()) # 判断如果文件能移返回True，否则返回False
print(f.readable()) # 判断文件是否可读
print(f.writable()) # 判断文件是否可写

# flush
# 打印进度条
import sys,time

for i in range(10):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(1)

# f.truncate() # 默认清空文件
# f.truncate(10) # 从文件开头截取10个字符
# f.seek(10)
# f.truncate(20) # 无论指针移到哪里，都从文件开头截取
"""

# f = open("yesterday", "r+", encoding="utf-8") # 文件句柄，读写模式，读模式打开，并可以追加写
# f = open("yesterday", "w+", encoding="utf-8") # 文件句柄，写读模式，写模式打开，并可以追加读
# f = open("yesterday", "a+", encoding="utf-8") # 文件句柄，追加读写模式
# f = open("yesterday", "wb") # 文件句柄，二进制写模式，视频要以二进制模式打开，网络传输要以二进制模式传输，跨平台要用到二进制
# f.write("binary\n".encode())
# f.close()
