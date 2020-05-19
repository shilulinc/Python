#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

def test(x,y,z):
    """testing"""
    print(x)
    print(y)
    print(z)

# test(1,2) # 位置参数与形参位置一一对应
# test(y=2,x=1) # 关键字参数与形参顺序无关
test(3,z=2,y=6) # 关键字参数必须在位置参数后面
