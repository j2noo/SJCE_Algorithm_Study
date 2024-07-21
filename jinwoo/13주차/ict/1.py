#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'perfectTeam' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING skills as parameter.
#

def perfectTeam(skills):
    dic = {"p":0,"c":0,"b":0,"m":0,"z":0}
    for skill in skills:
        print(skill)
        dic[skill]+=1
    
    ans=987654321
    for d in dic:
        ans=min(ans,dic[d])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    skills = input()

    result = perfectTeam(skills)

    fptr.write(str(result) + '\n')

    fptr.close()
