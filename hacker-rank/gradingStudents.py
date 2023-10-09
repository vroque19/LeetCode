#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        digit = grade % 10
        if grade >= 40 and digit < 5 and 5-digit < 3:
            grade += (10-2*digit)/2
            # print(grade)
        if grade >= 35 and digit > 5 and 10-digit < 3:
            grade += (10-digit)
        new_grades.append(int(grade))
    return new_grades
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
