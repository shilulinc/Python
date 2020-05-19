# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

# 复制文件
import shutil


# f1 = open("test.txt", encoding="utf-8")
# f2 = open("new_test.txt", "w", encoding="utf-8")
# shutil.copyfileobj(f1, f2)  # 复制已有文件内容到新文件，复制文件对象

# shutil.copyfile("test.txt", "new_test.txt")  # 复制已有文件内容到新文件，复制文件内容
# shutil.copystat("test.txt", "new_test.txt")

# shutil.copytree("src", "dst")  # 递归复制文件
# shutil.rmtree("tree")  # 递归删除目录
# shutil.make_archive("shutil_archive_test", "zip", "E:\Ansible")  # 压缩文件，压缩后的文件名/压缩格式/要压缩的文件

"""
# 压缩
import zipfile
z = zipfile.ZipFile("test.zip", "w")
z.write("test.txt")
print("in the zip")
z.close()
"""

"""
# 解压
import zipfile
z = zipfile.ZipFile("test.zip", "r")
z.extractall()
z.close()
"""
