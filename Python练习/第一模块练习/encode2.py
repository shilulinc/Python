#/usr/bin/env python
#_*_ coding:gbk _*_ # �˴������ļ�Ϊgbk�����ʽ��ʵ����python3�ڲ�Ĭ�ϵ���Ȼ��Unicode�����ʽ
__author__ = "Shi Lu"

import sys
print(sys.getdefaultencoding())

s = "����"
print(s)
print(s.encode("gb2312")) # ת����gb2312
print(s.encode()) # Ĭ��ת����utf-8
print(type(s.encode()))

gb2312_to_utf8 = s.encode("gb2312").decode("gb2312").encode("utf-8")
print(gb2312_to_utf8)
