#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0.000000
    zero = 0
    neg = 0
    tot = len(arr)
    
    for i in arr:
        if i == 0:
            zero += 1
        if i > 0:
            pos += 1
        if i < 0:
            neg += 1
    
    print("{:.6f}".format(pos/tot))
    print("{:.6f}".format(neg/tot))
    print("{:.6f}".format(zero/tot))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
