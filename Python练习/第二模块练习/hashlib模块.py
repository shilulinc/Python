# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

import hashlib
m = hashlib.md5()
m.update(b"hello")
# print(m.digest())  # 2进制格式hash
print(m.hexdigest())  # 16进制格式hash
m.update(b"It's me")
print(m.hexdigest())
m.update(b"It's been a long time since last time we ...")

m2 = hashlib.md5()
m2.update(b"helloIt's me")
print(m2.hexdigest())

s2 = hashlib.sha1()
m.update(b"helloIt's me")
print(s2.hexdigest())

import hmac
s3 = hmac.new(b"12345", "我爱北京天安门111".encode(encoding="utf-8"))
print(s3.digest())
print(s3.hexdigest())
