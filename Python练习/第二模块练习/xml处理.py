# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

import xml.etree.ElementTree as ET

tree = ET.parse("xml_test.xml")
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.text)

#只遍历year节点
for node in root.iter('year'):
    print(node.tag, node.text)
