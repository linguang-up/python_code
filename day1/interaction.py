#!/usr/bin/env python
# Author:Lin Guang
#密文密码,getpass模块在pycharm中无法正常执行，需要在命令行中执行

import getpass
db_name = "linguang"
db_passwd = "abc123.."


username = input("username:")
# password = getpass.getpass("password:")
password = input("password:")

if username == db_name and password == db_passwd :
    print("用户：%s，登录成功" %(username))

else :
    print("Invalid account password!")
