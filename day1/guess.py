#!/usr/bin/env python
# Author:Lin Guang


age_of_linguang = 30

guess_age = int(input("guess age:"))

if guess_age == age_of_linguang :
    print("you got it!")

elif guess_age > age_of_linguang :
    print("you must guess smaller!")

elif guess_age < age_of_linguang :
    print("you must guess bigger!!")

else:
    print("pls input type int!!!")