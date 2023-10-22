#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
 
def maximumPerimeterTriangle(sticks):
    sticks.sort()  # Sort the sticks in non-decreasing order

    max_perim = -1
    max_triangle = [max_perim]

    for i in range(len(sticks) - 2):
        if sticks[i + 2] < sticks[i] + sticks[i + 1]: # valid triangle
            perim = sticks[i] + sticks[i + 1] + sticks[i + 2]
            if perim > max_perim:
                max_perim = perim
                max_triangle = [sticks[i], sticks[i + 1], sticks[i + 2]]

    return max_triangle

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
