#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

# 递归函数的特点：1.有明确的结束条件 2.问题规模，每递归一次都应该比上一次问题规模有所减少，一次递归的越多，算法的效率就越高 3.效率低
"""
def calc(n):
    print(n)
    return calc(n+1)


calc(0) # 最大返回999
"""

"""
# 第一层函数还没执行完，就开始进入第二层函数...最后，return时再逐层往外返回
def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc(int(n/2))
    print("->", n)


calc(10)
"""