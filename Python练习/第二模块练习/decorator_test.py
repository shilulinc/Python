# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

gen = (i*2 for i in range(5))
print(gen)

for g in gen:
    print(g, end="-")
