# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

"""
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return "done"


fib(10)
"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b  # 保存当前生成器的运行状态并返回运行状态
        a, b = b, a + b
        n = n + 1
    return "done"  # 返回报错信息


g = fib(6)
while True:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break

# f = fib(10)
# print(f)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

# print("---start loop---")
# for i in f:
#     print(i)

res = filter(lambda n:n>5,range(10))
res = map(lambda n:n*2,range(10))
res = [lambda i:i*2 for i in range(10)]

import functools
res = functools.reduce(lambda x,y:x*y,range(1,10))
print(res)


a = {6:2,8:0,1:4,-5:6,99:11,4:22}
print(sorted(a.items()))
print(sorted(a.items(),key=lambda x:x[1]))


a = [1,2,3,4,5,6]
b = ['a','b','c','d']
for i in zip(a,b):
    print(i)
