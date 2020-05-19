# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

import xml.etree.ElementTree as ET


new_xml = ET.Element("namelist")
personinfo = ET.SubElement(new_xml, "personinfo",attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
sex = ET.SubElement(personinfo, "sex")
name.text = "Alex"
age.text = '22'
personinfo2 = ET.SubElement(new_xml, "personinfo2", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
age = ET.SubElement(personinfo2, "age")
name.text = "Rain"
age.text = '18'

et = ET.ElementTree(new_xml) #生成文档对象
et.write("test.xml",  encoding="utf-8", xml_declaration=True)

ET.dump(new_xml) #打印生成的格式
