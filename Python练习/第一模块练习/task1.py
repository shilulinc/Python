"""
f1 = open("C:\\Users\\石路\\Desktop\\test.txt", "a+")
f1.write("hahaha !"+"\n")
f1.close()
"""

"""
str = "Line1-abcdef Line2-abc Line4-abcd";
print(str.split("-"));
"""

"""
f = open("a.txt","w")
for i in range(1,10,2):
    f.write(str(i) +"\n")
f.close()

new = []
f = open("a.txt","r")
read = f.readlines()
for i in read:
    new_str = i.rstrip()
    new.append(new_str)
print(new)
f.close()
"""

"""
new = []
file = open("lock.txt","r+")
read_file = file.readlines()
for i in read_file:
    line = i.strip("\n")
    new.append(line)
print(new)
file.close()
"""