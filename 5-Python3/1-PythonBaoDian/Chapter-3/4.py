#!/usr/bin/env python3

import os,sys,time,math,re

# **,  *,  /,  //,  %,  +,  -,  |,  ^,  &,  <<,  >>


a1 = 'This is book.'
a2 = 'Nucleosome turnover'



print('1##########################################')
print( a1.join(a2) )   
print( 'AA'.join(a2) )   
print( 'AA'.join('dddd') )  

print('2##########################################')
print( a1.lower() )   
print( 'AA'.lower() )   
print( 'AAbbDD'.lower() )  


print('3##########################################')
print( a1.split() )  
print( a1.split(' is ') )  
print( 'AAcBBcRR'.split('c') )   
print( 'AAbbDD'.split('b') )  


print('4##########################################')
print( a1.swapcase() )  
print( 'AAcBBcRR'.swapcase() )   
print( 'AAbbDD'.swapcase() )  


print('5##########################################')
print( a1.title() )  
print( 'AAcB BcRR'.title() )   
print( 'AAb bDD'.title() )  


print('6##########################################')
print( a1.upper() )  
print( 'AAcB BcRR'.upper() )   
print( 'AAb bDD'.upper() )  



print('7##########################################')
print( len(a1) )  
print( len(a2) )
print( len('aa bb') )






