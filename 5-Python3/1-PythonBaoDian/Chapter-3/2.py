#!/usr/bin/env python3

import os,sys,time,math,re

# **,  *,  /,  //,  %,  +,  -,  |,  ^,  &,  <<,  >>


print(2**5, 2**0, 3*2, 4/2, 7/2, 7//2, 7%2, 4%2)

print(5|3) # 101 | 011 is 111 (7), 位或
print(9|17) # 01001 | 10001 is 11001 (25)
print(9|9) # 01001 | 01001 is 01001 (9)


print("######################################")
print(5^3) # 101 ^ 011 is 110 (6), 位异或
print(9^17) # 01001 ^ 10001 is 11000 (24)
print(9^9) # 01001 ^ 01001 is 00000 (0)




print("######################################")
print(5&3) # 101 & 011 is 001 (6), 位与
print(9&17) # 01001 & 10001 is 00001 (24)
print(9&9) # 01001 & 01001 is 01001 (0)


print("######################################")
print(2+3|5)  ##位运算的优先级最低。
print(2+3^5)  ##位运算的优先级最低。
print(2+3&5)  ##位运算的优先级最低。


print("######################################")
print(2+(3|5))  ##位运算的优先级最低。011 | 101
print(2+(3^5))  ##位运算的优先级最低。
print(2+(3&5))  ##位运算的优先级最低。

