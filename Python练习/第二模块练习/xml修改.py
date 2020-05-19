# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

import xml.etree.ElementTree as ET

tree = ET.parse("xml_test.xml")
root = tree.getroot()

#修改
# for node in root.iter("year"):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated", "yes")
#
# tree.write("xml_test.xml")

#删除node
for country in root.findall('country'):

    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')
