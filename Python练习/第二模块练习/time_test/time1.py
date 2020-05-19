# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

import time
x = time.localtime()
print(x)
print(x.tm_year)
print(time.strftime("%Y-%m-%d %H:%M:%S", x))  # %Y:x.tm_year  %m:x.tm_mon
print(time.strptime("2018-01-29 21:08:08", "%Y-%m-%d %H:%M:%S"))
