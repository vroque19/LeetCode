#!/bin/python3


import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()
    curr = a[0]
    window = [curr]
    for i in range(1, len(a)):
        if a[i] == curr:
            window.append(a[i])
        else:
            if len(window) == 1:
                return a[i-1]
            curr = a[i]
            window = [curr]
        print(window)
    return window[0]
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
