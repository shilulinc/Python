# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

"""
# 生成随机数 version1
import random

check_code = ""
for i in range(4):
    current = random.randint(1, 9)
    check_code += str(current)
print(check_code)
"""

import random
check_code = ""
for i in range(4):
    current = random.randrange(0, 4)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(0, 9)
    check_code += str(tmp)
print(check_code)
