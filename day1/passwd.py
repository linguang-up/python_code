#!/usr/bin/env python
# Author:Lin Guang

name = input("name:")
age = input("age:")
salary = input("salary:")

# info = '''------------information  %s ------------
# NAME:%s
# AGE:%s
# salary:%s
# ''' % (name,name,age,salary)

info = '''------------information  {_name} ------------
NAME:{_name}
AGE:{_age}
salary:{_salary}
'''.format (_name=name,_age=age,_salary=salary)

print(info)