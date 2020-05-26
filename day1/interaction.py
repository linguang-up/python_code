#!/usr/bin/env python
# Author:Lin Guang
#密文密码,getpass模块在pycharm中无法正常执行，需要在命令行中执行

import getpass

username = input("username:")
password = getpass.getpass("password:")

print("username",password)
