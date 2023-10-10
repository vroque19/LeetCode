#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    to_binary = toBinary(n)
    binary = "0"*(32-len(to_binary)) + to_binary
    ans = ""
    for i in range(len(binary)):
        if binary[i] == "0":
            ans += "1"
        else:
            ans += "0"
    sol = toDecimal(ans)
    return sol

def toDecimal(binary):
    answer = 0
    print(answer)
    j = 1
    for i in binary:
        val = int(i)*(2**(len(binary)-j))
        answer = int(answer) + int(val)
        j+=1
    return int(answer)
    
def toBinary(decimal):
    if decimal == 0:
        return "0"
    if decimal == 1:
        return "1"
    return toBinary(decimal//2) + str(decimal % 2)
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
