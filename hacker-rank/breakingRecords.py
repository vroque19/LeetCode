#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_count = 0
    max_count = 0
    min_score = max_score = scores[0]
    records_broke = []
    for score in scores:
        if min_score > score:
            min_score = score
            min_count += 1
        if max_score < score:
            max_score = score
            max_count += 1
    records_broke.append(max_count)
    records_broke.append(min_count)
    return records_broke
    
    # Write your code here
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
