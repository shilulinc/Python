#/usr/bin/env python
#_*_ coding:utf-8 _*_
__Author__ = "Shi Lu"

name = "my \tname is {name} and my age is {years} old"
# print(name.capitalize()) # 首字母大写
# print(name.count("a")) # 统计字母a出现的次数
# print(name.center(50, "-")) # 打印50个字符，以"-"补齐，并把内容放在中间
# print(name.endswith("ex")) # 判断字符串是否以"ex"结尾
# print(name.expandtabs(tabsize=30)) # 把"tab"键转为30个空格
# print(name.find("name")) # 查找"name"的索引
# print(name[name.find("name"):]) # 切割字符串，以"name"开始到字符串结束
# print(name.format(name="alex", years=23)) # 格式化输出
# print(name.format_map({"name":"alex", "years":23})) # 以字典的形式进行格式化输出
# print("abc123".isalnum()) # 判断字符串"abc123"是否至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
# print("Abc".isalpha()) # 判断字符串"Abc"是否至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
# print("1A".isdecimal()) # 判断字符串"1A"是否只包含十进制字符
# print("1A".isdigit()) # 判断字符串"1A"是否只由数字组成
# print("1A".isidentifier()) # 判断字符串是否一个合法的标识符
# print("abc".islower()) # 判断字符串是否小写
# print("22".isnumeric()) # 判断字符串"22"是否纯数字 和isdigit()方法相似
# print("abc".isspace()) # 判断字符串"abc"是否空格
# print("My Name Is Alex".istitle()) # 判断字符串"My Name Is Alex"是否首字母大写，其余字母小写
# print("abc".isprintable()) # 判断字符串"abc"是否可打印 在字符串中不用，可判断tty file, drive file是否可打印
# print("ABC".isupper()) # 判断字符串"ABC"是否大写
# print(",".join(["1", "2", "3"])) # 把列表["1", "2", "3"]转换成字符串
# print(name.ljust(50, "-")) # 靠左打印50个字符，不足以"-"补齐
# print(name.rjust(50, "-")) # 靠右打印50个字符，不足以"-"补齐
# print("Alex".lower()) # 把大写转换成小写
# print("Alex".isupper()) # 把小写转换成大写
# print("\nAlex".lstrip()) # 从左边删除空格和换行
# print("Alex\n".rstrip()) # 从右边删除空格和换行
# print("\nAlex\n") # 从两边删除空格和换行
# p = str.maketrans("abcd", "1234") # 把后面的数字和前面的字母对应
# print("alex".translate(p)) # 打印出来替换字符串"alex"中包含替换的字符
# print("alex li".replace("l","L")) # 把字符串中的小写"l"替换成大写"L"
# print("alex li".rfind("l")) # 从左向右取"l"，取到最右边的字符串的索引
# print("1+2+3+4".split("+")) # 以符号"+"分片分隔成列表
# print("1+2\n+3+4".splitlines()) # 以换行符"\n"分片分隔成列表
# print("Alex Li".swapcase()) # 小写变成大写，大写变成小写
# print("alex li".title()) # 首字母大写，变成标题
# print("Alex Li".zfill(50)) #不够用零填充
