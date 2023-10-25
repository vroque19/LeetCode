#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    min = a[0]
    count = 1
    prev_count = 0
    
    for i in range(1, len(a)):
        if a[i] == min or a[i] == min+1:
            count += 1
        elif prev_count <= count:
            prev_count = count
            count = 1
            min = a[i]
    if prev_count == 0:
        return count
    return prev_count
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
