#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def countNums(arr, result):
    for num in arr:
        result[num] += 1
def countingSort(arr):
    freq_arr = [0]*100
    print(freq_arr)
    # sorted = []
    countNums(arr, freq_arr)
    return freq_arr
    # this returns the sorted arr
    # for i in range(len(freq_arr)):
    #     sorted.extend([i]*freq_arr[i])
    # return sorted
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
