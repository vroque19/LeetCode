#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    dict = {}
    valid_segments = []
    for i in range(len(s)-m+1):
        dict[tuple(s[i:i+m])] = sum(s[i:i+m])
    # print(dict)
    for key, val in dict.items():
        # print(key)
        if val == d:
            valid_segments.append(key)
    print(f"Segments with the value '{d}': {valid_segments}")
    
    return len(valid_segments)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
