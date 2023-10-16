#!/usr/bin/env python3

import sys
import base64
import binascii
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

cText = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ans = ""
key="myXORkey"
count=0
counter=0
keycount=0
while counter<len(cText):
    ansbin=""
    keyset = bin(ord(key[keycount%8]))[2:]
    current = cText[counter] + cText[counter+1]
    currentbin = bin(int(current, 16))[2:]
    while len(currentbin)>len(keyset):
        keyset = "0"+keyset
    while len(currentbin)<len(keyset):
        currentbin = "0"+currentbin
    for count2 in range(len(keyset)):
        ansbin += str(int(not keyset[count2]==currentbin[count2]))
    ans += chr(int(ansbin, 2))
    counter+=2
    keycount+=1

print("The flag is:\n" + ans)