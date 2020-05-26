#!/usr/bin/env python
# Author:Lin Guang


count = 0
while count < 4:    #当count<4条件不成立的情况下执行else
    print("进while，%s" % count)
    count += 1

else:
    print("进else,%s" % count)