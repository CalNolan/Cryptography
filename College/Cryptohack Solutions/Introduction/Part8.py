#!/usr/bin/env python3

import sys
import base64
import binascii
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
ans = ""
final= ""
newnum=0

key1bin = bin(int(key1, 16))[2:]
key23bin = bin(int(key23, 16))[2:]
flagbin = "00000"+bin(int(flag,16))[2:]
count=0

for dig in range(len(flagbin)):
    masterkey = key1bin[dig]==key23bin[dig]
    if int(not masterkey)==int(flagbin[dig]):
        final+="0"
    else:
        final+="1"
print("hello\n" +final)
print(str(len(final)))

for i in range(len(final)):
    newnum += int(final[i]) * 2**(len(final)-i-1)
print(hex(newnum)[2:])
ans = bytes.fromhex(hex(newnum)[2:])

print("Here is your flag:")
print(str(ans)[2:-1])
