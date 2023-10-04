#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    combos = list(combinations(arr, 4))
    sums = []
    for comb in combos:
        sums.append(sum(comb))
    print(min(sums), max(sums))
        
        
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
