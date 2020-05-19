# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

import re
p = re.compile("^[0-9]")
m = p.match("14534Abc")
print(m.group())
