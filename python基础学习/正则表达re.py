#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sam'

import re

# findall 匹配所有 返回所有匹配内容
ret = re.findall("\w+", "a8@979_32~fsd%8sdh990")
ret = re.findall("[0-9]+", "a8@979_32~fsd%8sdh990")
ret = re.findall("[a-zA-Z]+", "a8@979_32~fsd%8sdh990")
print ret

# match 只能匹配开头 返回对象
ret = re.match("[a-zA-Z]+", "a8@979_32~fsd%8sdh990")
if ret:
    print ret
    print ret.group()

# search 用法同match 但是可以匹配任意位置
ret = re.search("\d+", "a8@979_32~fsd%8sdh990")
ret = re.search("~", "a8@979_32~fsd%8sdh990")
if ret:
    print ret
    print ret.group()

# sub 替换匹配字符
ret = re.sub("\d+", "*", "a8@979_32~fsd%8sdh990")
# count表示替换的个数
ret = re.sub("\d+", "*", "a8@979_32~fsd%8sdh990", count=2)
print ret

# ^开头匹配 $结尾匹配
ret = re.search("^[a-z]", "a8@979_32~fsd%8sdh990")
ret = re.search("\d$", "a8@979_32~fsd%8sdh990")
print ret.group()