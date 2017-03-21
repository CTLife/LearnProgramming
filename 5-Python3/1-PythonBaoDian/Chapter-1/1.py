#!/usr/bin/env python3
import os

print("Hello, Python !")
os.system('python3 -V')
os.system('sleep  2s')
print('python version >= 3.5.0')

print("\n\n########################################")

print(dir(os))   ##List the functions in module os.

print("########################################\n\n")

## https://docs.python.org/3/library/os.html?highlight=os#module-os

print( os.times() )  ##Returns the current global process times.



