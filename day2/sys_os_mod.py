#!/usr/bin/env python
# Author:Lin Guang

import sys

print(sys.path)     #打印python环境变量，导入模块时查找的路径
print(sys.argv)     #接收传参
# print("----->",sys.argv[2])

import os
cmd_res=os.system("dir")   #执行操作系统命令，在屏幕打印结果，返回值为0、1
print(cmd_res)
print(os.popen("dir"))    #执行操作系统命令，结果暂存在内存，返回值为内存地址
print(os.popen("dir").read())  #使用read方法，读取内存地址中的内容
os.mkdir("new_dir")