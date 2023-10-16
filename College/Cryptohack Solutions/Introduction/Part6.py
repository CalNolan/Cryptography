#!/usr/bin/env python3

import sys
import base64
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

num1 = 13
string = "label"
ans = ""
num1 = "000"+bin(num1)[2:]
for index in range(len(string)):
    binords = bin(ord(string[index]))[2:]
    bincomp = ""
    for dig in range(len(binords)):
        if binords[dig]==num1[dig]:
            bincomp = bincomp + "0"
        else:
            bincomp = bincomp + "1"
    ans += chr(int(bincomp, 2))
    
#string2 = str(bytes.fromhex(str(string)).decode('utf-8'))

print("Here is your flag:")
print("crypto{"+ans+"}")
