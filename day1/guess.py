#!/usr/bin/env python
# Author:Lin Guang


age_of_linguang = 30


count = 0
while count < 5:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_linguang :
        print("you got it!")
        exit()

    elif guess_age > age_of_linguang :
        print("you must guess smaller!")

    elif guess_age < age_of_linguang :
        print("you must guess bigger!!")

    else:
        print("pls input type int!!!")

    count += 1

print("输入次数太多，请重新开始！")