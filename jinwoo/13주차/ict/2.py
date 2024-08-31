#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'raisingPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
MOD = 10**9 + 7
def raisingPower(arr):
    ans=-1
    ansIdx=-1
    print(arr)
    for i in range(len(arr)-1):
        calc = (arr[i]**arr[i+1])% MOD
        print("Calc:",calc)
        if calc>ans:
            ans=calc
            ansIdx = i+1
    return ansIdx
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = raisingPower(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
