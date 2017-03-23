#!/usr/bin/env python3

import os,sys,time,math,re

# **,  *,  /,  //,  %,  +,  -,  |,  ^,  &,  <<,  >>


a1 = 'This'
a2 = 'Nucleosome turnover in adult heart.'



print('1##########################################')
print( a1.join("---") )   
print( a1.join("--") ) 
print( a1.join("-") )   
print( '_'.join("a1") ) 
print( '_'.join(a1) ) 



print('2##########################################')

## 以空格分割的3种写法：
print( a2.split(' ') ) 
print( a2.split(None) ) 
print( a2.split() ) 

print( a2.split(None, 20) ) 

print( a2.split(None, 2) ) 
print( a2.split(None, 1) ) 
print( a2.split(None, 0) ) 








