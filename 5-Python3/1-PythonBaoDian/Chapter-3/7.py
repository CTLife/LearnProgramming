#!/usr/bin/env python3

import os,sys,time,math,re



myStr1 = 'So %d day!'   ##可以被10进制整数取代
myStr2 = 'So %o day!'   ##可以被8进制整数取代
myStr3 = 'So %f day!'   ##可以被10进制浮点数取代
myStr4 = 'So %x day!'   ##可以被16进制整数取代， a-f小写
myStr5 = 'So %X day!'   ##可以被16进制整数取代， a-f大写
myStr6 = 'So %c day!'   ##可以被单个字符取代
myStr7 = 'So %s day!'   ##可以被字符串取代
 


print('1##########################################')
print( myStr1 % 12 )  
print( myStr1 % 18.693 )    
print( myStr2 % 12 )   
print( myStr3 % 18.693 )    
print( myStr4 % 12 ) 
print( myStr5 % 12 ) 
print( myStr6 % 'a' ) 
print( myStr7 % 'very good' ) 

 
print('2##########################################')
print( int('10')+5 )  
print( '10'+str(5) )  


print('3##########################################')
path1 = r'/home/yp/Desktop/'
print( os.listdir(path1) )

path2 = r'/home\/yp/Desktop/'
print( os.listdir(path2) )



