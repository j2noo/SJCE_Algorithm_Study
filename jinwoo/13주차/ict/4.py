#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSchedules' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER workHours
#  2. INTEGER dayHours
#  3. STRING pattern
#
import sys
sys.setrecursionlimit(10**6)

li = []
def recur(depth, ptrn):
    if depth>7 :
        li.append(ptrn)
        return
    for i in range(9):
        newPtrn = str(ptrn) + str(i)
        recur(depth+1,newPtrn)
def findSchedules(workHours, dayHours, pattern):
    # Write your code here
    ans=[]
    ptrn = ""
    recur(1,ptrn)
    
    # print(li)
    for ptrn in li:
        
        # print("!#",ptrn)
        nums = list(map(int,ptrn))
            # validation ~
        sums = sum(nums)
        maxHours = max(nums)
        validFlag=1
        for i in range(len(nums)):
            if not ( pattern[i]=='?' or ptrn[i]==pattern[i]):
                validFlag=0
        if sums == workHours and maxHours<= dayHours and validFlag==1:
            ans.append(ptrn)
            # print("!!",ptrn)
        # print(ptrn,"sums : ",sums, "maxH : ",maxHours, "Vailid :",validFlag)
            
            
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    workHours = int(input().strip())

    dayHours = int(input().strip())

    pattern = input()

    result = findSchedules(workHours, dayHours, pattern)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
