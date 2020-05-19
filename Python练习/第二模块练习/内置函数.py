# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

# print(all([0, -5, 3]))  # Python中非零为真，零为假
# print(all([1, -5, 3]))
# print(any([0, -5, 3]))
# a = ascii([0, -5, 3])
# print(type(a ), [a])
# print(bin(2))  # 十进制整数转换为二进制
# print(bool([])) # 判断真假，零、空列表和空字典为假

"""
a = bytes("abcde", encoding="utf-8")  # 变为二进制，不可修改
print(a.capitalize(), a)
"""

"""
b = bytearray("abcde", encoding="utf-8")  # 变为二进制数组，可以修改
b[1] = 50  # 需要指定ASCII码中的顺序
print(b)
"""

# def test():pass
# print(callable(test))  # 判断是否可调用，只要后面可以加()，就可以被调用
# print(chr(97))  # 输出ASCII码中对应的字符
# print(ord("a"))  # 输出ASCII码中对应的顺序

"""
code = "for i in range(10):print(i)"
print(code)
c = compile(code, "", "exec")
exec (c)
"""

'''
code = """
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

"""
# 第一种方法：
py_obj = compile(code, "err.log", "exec")
exec(py_obj)

# 第二种方法：
exec(code)
'''

# print(divmod(5, 1))  # 返回5/1组成的元组结果，商为5，余数为0

# def sayhi(n):
#     print(n)
#     for i in range(n):
#         print(i)
# sayhi(3)
#
# # calc = lambda n:print(n)
# # calc(3)
#
# calc = lambda n:3 if n < 4 else n
# print(calc(4))

# 按条件过滤
# res = filter(lambda n:n > 5, range(10))
# res = map(lambda n:n * 2, range(10))
# res = [ lambda n:n * 2 for i in range(10) ]
# for i in res:
#     print(i)
#
# a = [ i*2 for i in range(10) ]
# print(a)

"""
import functools
res = functools.reduce(lambda x, y:x + y, range(10))
print(res)
"""

# a = set([1,2,3,3,4,4,5])  #可变
# b = frozenset([1,2,3,3,4,4,5])  # 不可变

# print(globals()) # 以字典形式返回当前程序key:value键值对
# print(locals())  # 返回局部变量

"""
def test():
    local_var = 333
    print(locals())
    print(globals())
test()
"""

# print(hex(1))  # 十六进制
# print(oct(1))  # 八进制
# print(pow(2, 8))  # 返回2**8
# print(repr("a"))  # 把一个对象转成字符串
# print(round(1.333, 2))  # 精确到小数点后两位
# print(range(10)[slice(2, 5)])  # 截取指定的列表

"""
a = {6:2, 3:5, 8:6, 16:8, 11:22, 66:88}
print(a.items())
print(sorted(a.items()))  # 默认按key进行升序排序
print(sorted(a.items(), key=lambda x:x[1]))  # 使用lambda按value进行升序排序
"""

"""
a = [1, 2, 3, 4, 5, 6]
b = ["a", "b", "c", "d"]
for i in zip(a, b):
    print(i)
"""

# import decorator  # 导入模块
# __import__("decorator")  # 导入字符串
