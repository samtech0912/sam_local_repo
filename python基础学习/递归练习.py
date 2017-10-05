#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sam'

import os
import sys

def func(directory):
    if not isinstance(directory, str):
        print "Input error! Please input a string."
        sys.exit(1)
    if not os.path.exists(directory):
        print "The directory [%s] do not exist !" %directory
        sys.exit(1)
    else:
        print "The directory is [%s]." %directory
        getFileSize(directory)

# 若为文件 则得该文件大小 若为文件夹 则获得该文件夹内每一个文件的大小
def getFileSize(f):
    if os.path.isdir(f):
        print "[folder] %s" %f
        for i in os.listdir(f):
            if i:
                ff = f + "/" + i
                getFileSize(ff)
    elif os.path.isfile(f):
        filesize = os.path.getsize(f)/1024
        filename = f.split("/")[-1]
        print "[file] %s --> %.1f KB" %(filename, filesize)

if __name__ == "__main__":
    func("D:\python")