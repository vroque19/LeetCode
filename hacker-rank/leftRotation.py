#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    n = len(arr)
    curr = 0
    res = [0 for _ in range(n)]
    for i in range(n-d):
        res[i] = arr[d + i]
        # print(res, i, d)
        curr += 1
    for i in range(n-curr):
        res[curr] = arr[i]
        curr +=1
    return res
        
    
    # while d > 0:
    #     for i in range(n-1):
    #         temp = arr[i+1]
    #         arr[i+1] = arr[i]
    #         arr[i] = temp
    #     d = d - 1
    # return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
