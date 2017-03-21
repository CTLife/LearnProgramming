#!/usr/bin/env python3

import os,sys,time,math,cmath,re


## https://docs.python.org/3/library/math.html?highlight=math#module-math
## all functions in math:
x=2.2
y=3.3

print("# 0 ###########")
print(math.ceil(x), math.copysign(x, y),  math.fabs(-x), math.factorial(12), math.floor(x))
print("# 1 ###########")
print(math.ceil(-x), math.copysign(-x, -y),  math.fabs(-x), math.factorial(1000), math.floor(-x))
print("# 2 ###########")
print(math.copysign(x, 1),  math.copysign(x, -1), math.copysign(x, 0), math.copysign(x, -0),  math.copysign(x, -0.0))
print("# 3 ###########")
print(math.copysign(-x, 1),  math.copysign(-x, -1), math.copysign(-x, 0), math.copysign(-x, -0),  math.copysign(-x, -0.0))

print("# 4 ###########")
#print(math.factorial(100000))


print("# 5 ###########")
print(math.fmod(x, y), x%y)   ##返回参数x/y的余数
print(math.fmod(5, 2), 5%2)   ##返回参数x/y的余数

print("# 6 ###########")
print( math.frexp(220) )   ## 
print( math.frexp(4) )   ##返回参数x/y的余数

print("# 7 ###########")
print( sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]) )  
print( math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]) )
print( sum([0.2, 0.5]) )  
print( math.fsum([0.2, 0.5]) )
print( sum([0.2, 0.5, 0.33]) )  
print( math.fsum([0.2, 0.5, 0.33]) )


print("# 8 ###########")
print( math.gcd(42, 45) )   #最大公约数 
print( math.gcd(4, 6) )
print( math.gcd(12, 18) )
print( math.gcd(35872, 1859746) )



print("# 8 ###########")
print( 42*45/math.gcd(42, 45) )   #最小公倍数 
print( 4*6/math.gcd(4, 6) )
print( 12*18/math.gcd(12, 18) )
print( 35872*1859746/math.gcd(35872, 1859746) )




#math.copysign(x, y):
## Return a float with the magnitude (absolute value) of x but the sign of y. 
## On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0.


#math.frexp(x):
## Return the mantissa and exponent of x as the pair (m, e). m is a float and e is an integer such that x == m * 2**e exactly. 
## If x is zero, returns (0.0, 0), otherwise 0.5 <= abs(m) < 1. This is used to “pick apart” the internal representation 
## of a float in a portable way.


#math.gcd(a, b)
## Return the greatest common divisor of the integers a and b.



##设两个数a,b的最大公约数是p,最小公倍数是q, 那么:ab=pq





