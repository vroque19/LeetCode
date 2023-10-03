#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    sums = []
    last_index = len(arr)//2 + 1
    for i in range(last_index):
        for j in range(last_index):
            sums.append(getHourglass(arr, i, j, last_index))
    return max(sums)    

def getHourglass(arr, row, col, end):
    top = 0
    middle = 0
    bottom = 0
    for i in range(col, end+col-1):
        top += arr[row][i]
    middle += arr[row+1][col+1]
    for i in range(col, end+col-1):
        bottom += arr[row+2][i]
    # print(top, middle, bottom, '\n')
    return top + middle + bottom
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
