#!/usr/bin/env python3

import os,sys,time,math,re


a=66
b=3

c1=a*2\
  +b\
  -b\
  *3

c2=(a*2  #也可以使用圆括号把一条语句写在多行。
  +b 
  -b 
  *3)


print(c1, c2)



print('\n\n###################################################################\n')
中国 = "China"
print(中国)

中国1 = "中国"
print(中国1)

中国_china = "中国_China"
print(中国_china)


print('\n\n###################################################################\n')
name = input('Please input your name:')
print('Hi', name)
print('\n\n###################################################################\n')



# 定义和输出列表
list1 = [1, 2, 3, 4, 5]
list2 = ['1a', '2aa', '3aaa', '4aaaa', '5aaaaa']
print(list1)
print(list2)


# 定义和输出元组
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('1a', '2aa', '3aaa', '4aaaa', '5aaaaa')
print(tuple1)
print(tuple2)



print('\n\n###################################################################\n')
# 同时输出列表和元组
print(list1, list2, '\n', tuple1, tuple2)














