#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
# 97-122
    
def encrypt(c):
    lower = {}
    upper = {}
    for i in range(26):
        if i+k >= 26:
            upper[i+65]=65+((i+k)-26)
        else:
            upper[i+65] = (i+65+k)
    for i in range(26):
        if i+k >= 26:
            lower[i+97]=97+((i+k)-26)
        else:
            lower[i+97] = (i+97+k)
    print(lower)
    print(upper)
            
    if ord(c) in lower:
        c = chr(lower[ord(c)])
    if ord(c) in upper:
        c = chr(upper[ord(c)])
    return c
def caesarCipher(s, k):
    new_string = ""
    for c in s:
        c_prime = encrypt(c)
        new_string += c_prime
    return new_string
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
