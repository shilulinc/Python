#/usr/bin/env python
#_*_ coding:utf-8 _*_
__Author__ = "Shi Lu"

# key-value
info = {
    "stu101": "Wu Tenglan",
    "stu102": "Longze Luola",
    "stu103": "Xiaoze Maliya",
}
print(info)
# print(info["stu101"])
info["stu101"] = "武藤兰"
print(info)
info["stu104"] = "Cang Jingkong" # 如果存在就修改，如果不存在就创建
print(info)

# del
# del info["stu101"]
info.pop("stu101") # 删除指定的键值对
info.popitem() # 随机删除一个键值对
# print(info)

# print(info["stu105"]) # 查找指定的键值对，如没有则会报错
print(info.get("stu105")) # 查找指定的键值对，如没有则会输出"None"
print("stu103" in info) # 在Python2.7中，等同于info.has_key("stu103")

av_catalog = {
    "欧美": {
        "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
        "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "x-art.com": ["质量很高,真的很高", "全部收费,屌比请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "听说是收费的"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] = "可以在国内做镜像"
print(av_catalog)
# keys
print(av_catalog.keys()) # 把keys打印成列表
# values
print(av_catalog.values()) # 把values打印成列表
# setdefault
av_catalog.setdefault("台湾", ["www.baidu.com"]) # 没有键值对时定义新键值对
print(av_catalog)
av_catalog.setdefault("台湾", "百度") # 有键值对时使用已有的键值对
print(av_catalog)
# update
d1 = {
    "stu101": "Alex",
    "1": "3",
    "2": "4",
}
print(d1)
av_catalog.update(d1) # 对字典合并，没有的键值对会被增加，已有的键值对会被更新
print(av_catalog)
# items
print(av_catalog.items()) # 对字典中的每个键值对生成元组，并生成大的列表

d2 = info.fromkeys(["6", "7", "8"], "test") # 初始化字典，重新生成新字典
print(d2)
