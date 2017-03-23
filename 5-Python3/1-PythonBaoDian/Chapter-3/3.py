#!/usr/bin/env python3

import os,sys,time,math,re

# **,  *,  /,  //,  %,  +,  -,  |,  ^,  &,  <<,  >>


a1 = 'This is book.'
a2 = 'Nucleosome turnover'
print(a1+a2)
print(a2+'is essrntial for ......')

print(a1*3)


print('##########################################')

b1 = "hi, python!"
print( b1.capitalize() )  #第1个字母大写
print( b1.count('h') )  #substring的数目
print( b1.count('th') )  #substring的数目
print( b1.count('thk') )  #substring的数目

print( b1.find('h') )  #substring的起始位置
print( b1.find('th') )  #substring的起始位置
print( b1.find('thk') )  #substring的起始位置, 这里返回-1



print('##########################################')
print( b1.isalnum() )   # only conteins "0-9A-Za-z" ?
print( 'nucleosome'.isalnum() )   # only conteins "0-9A-Za-z" ?
print( b1.isalpha() )   # only conteins "A-Za-z" ?
print( 'nucleosome'.isalpha() )   # only conteins "A-Za-z" ?
print( b1.isdigit() )   # only conteins "0-9" ?
print( '1233456'.isdigit() )   # only conteins "0-9" ?

print('##########################################')
print( b1.islower() )   # only conteins "a-z" ?   只考察字母
print( 'Vnucleosome12'.islower() )   # only conteins "a-z" ?  只考察字母
print( b1.isspace() )   # only conteins " " ?
print( ' 	'.isspace() )   # only conteins " " ?
print( b1.isupper() )   # only conteins "A-Z" ?  只考察字母
print( 'AVFRTC12365'.isupper() )   # only conteins "A-Z" ? 只考察字母


print('##########################################')
print( b1.istitle() )   # 单词的首字母是否为大写？
print( 'Nucleosme Turnover is correlated with'.istitle() )   # 单词的首字母是否为大写？
print( 'Nucleosme Turnover Is Correlated With'.istitle() )   # 单词的首字母是否为大写？









