#/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author="Shi Lu"

# 打印1-10乘法表
"""
for i in range(1,10):
    for j in range(i):
        j += 1
        print("%d * %d = %-2d" % (i, j, i*j))
    print("results")
"""

# 打印1-100之间的偶数
"""
start =1
while True:
    print(start*2)
    start +=1
    if start == 51:
        break
"""

# 打印1-100之间的奇数
"""
start = 1
while True:
    if start%2 == 1:
        print(start)
    start += 1

    if start == 100:
        break
"""

#定义初始值,sum指的是总和，start指的是1-100的整数
"""
sum=0
start=1
while True:
   if start==101:
     break
#%运算是取余数，判断是奇数还是偶数
   if start%2 ==1:
     sum += start
   if start%2 ==0:
     sum -= start
   start +=1
print(sum)
"""
