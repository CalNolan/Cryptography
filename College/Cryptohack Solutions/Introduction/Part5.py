#!/usr/bin/env python3

import sys
import base64
from Crypto.Util.number import *
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

string = long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269)
print(string)
#string2 = str(bytes.fromhex(str(string)).decode('utf-8'))

print("Here is your flag:")
#print("".join(string2))
