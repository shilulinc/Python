# /usr/bin/env python
# _*_ coding:utf-8 _*_
# Author = "Shi Lu"

import configparser
config = configparser.ConfigParser()
config.read("example.ini")
# print(config.read("example.ini))
# print(config.default_section)
# print(config.defaults())
# print(config.sections())
# print(config["bitbucket.org"]["user"])
for key in config['bitbucket.org']:
    print(key)
