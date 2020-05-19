#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Shi Lu"

"""
def load_dict_from_file(filepath):
    _dict = {}
    try:
        with open(filepath, 'r') as dict_file:
            for line in dict_file:
                (key, value) = line.strip().split(':')
                _dict[key] = value
    except IOError as ioerr:
        print "文件 %s 不存在" % (filepath)
     
    return _dict
 
def save_dict_to_file(_dict, filepath):
    try:
        with open(filepath, 'w') as dict_file:
            for (key,value) in _dict.items():
                dict_file.write('%s:%s\n' % (key, value))
    except IOError as ioerr:
        print "文件 %s 无法创建" % (filepath)
 
if __name__ == '__main__' :
    _dict = load_dict_from_file ('dict.txt')
    print _dict
    save_dict_to_file(_dict, 'dict_copy.txt')
"""

d = {}
f = open("users_info", "r+", encoding="utf-8")
for i in f:
    (key, value) = i.strip("\n").split(":", 1)
    d[key] = value
print(d)
