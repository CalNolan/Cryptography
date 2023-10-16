#!/usr/bin/env python3

import sys
import base64
import binascii
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

cText = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
ans = ""

#We know that the plaintext is in the format "cypto{FLAG}", so the first char is c

startbin=bin(int("73", 16))
cbin=bin(ord("c"))

print(startbin + "\n" + cbin)

key = int(startbin[2:])^int(cbin[2:])

print(key)
counter=0
while counter<len(cText):
    print(counter)
    ansbin=""
    keyset = str(key)
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

print("The flag is:\n" + ans)