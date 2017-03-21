#!/usr/bin/env python3

import os,sys,time,math,cmath,re,cmath


## https://docs.python.org/3/library/cmath.html?highlight=cmath#module-cmath
## all functions in cmath:
x=2.2
y=3.3

z = x + y*1j
print(z, z.real,  z.imag)

z1 = complex(-x, y)
print(z1, z1.real,  z1.imag)
print("#####################################")

## polar coordinates:
print( cmath.phase(z),  cmath.phase(z1)  )
print( cmath.polar(z), cmath.polar(z1) )
print( (abs(z), cmath.phase(z)),    (abs(z1), cmath.phase(z1)) )

print("#####################################")
print( cmath.rect(5, 1),  cmath.rect(50, 10) )

print(cmath.pi,  cmath.e)

print(z*10)


