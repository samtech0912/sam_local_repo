#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sam'

# 输出列表
print "输出列表"
l = [i for i in range(4)]
print l
print "-"*30

# 输出二维列表
print "输出二维列表"
l = [[i for i in range(4)] for j in range(4)]
for ll in l:
    print ll
print "-"*30

# 二维列表旋转
print "二维列表旋转"
data = [[i for i in range(4)] for j in range(4)]
for d in data:
    print d
print "-"*30
for row_index, row in enumerate(data):
    for col_index in range(row_index, len(row)):
        tmp = data[col_index][row_index]
        data[col_index][row_index] = data[row_index][col_index]
        data[row_index][col_index] = tmp
for d in data:
    print d