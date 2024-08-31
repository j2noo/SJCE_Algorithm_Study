#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'doesCircleExist' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY commands as parameter.
#

# see : [0,1,2,3] 상우하좌
dy = [-1,0,1,0]
dx = [0,1,0,-1]
def solve(cmds):
    # 초기 상태
    ansFlag=0
    r,c,see=100,100,0
    see = 0
    # 1 try
    for cmd in cmds:
        if cmd=='G':
            r = r + dy[see]
            c = c + dx[see]
        elif cmd=='R':
            see = (see+1)%4
        elif cmd=='L':
            see = (see-1)%4
    if r==100 and c==100 and see==0 :
        ansFlag=1
        
    # 2 try
    for cmd in cmds:
        if cmd=='G':
            r = r + dy[see]
            c = c + dx[see]
        elif cmd=='R':
            see = (see+1)%4
        elif cmd=='L':
            see = (see-1)%4
    if r==100 and c==100 and see==0 :
        ansFlag=1
        
    # 3 try
    for cmd in cmds:
        if cmd=='G':
            r = r + dy[see]
            c = c + dx[see]
        elif cmd=='R':
            see = (see+1)%4
        elif cmd=='L':
            see = (see-1)%4
    if r==100 and c==100 and see==0 :
        ansFlag=1
        
    # 4 try
    for cmd in cmds:
        if cmd=='G':
            r = r + dy[see]
            c = c + dx[see]
        elif cmd=='R':
            see = (see+1)%4
        elif cmd=='L':
            see = (see-1)%4
    if r==100 and c==100 and see==0 :
        ansFlag=1
    
    return ansFlag
       

    
def doesCircleExist(commands):
    # Write your code here
    ans=[]
    for command in commands:
        print("@",command)
        ret = solve(command)
        if ret==0:
            ans.append("NO")
        else :
            ans.append("YES")
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    commands_count = int(input().strip())

    commands = []

    for _ in range(commands_count):
        commands_item = input()
        commands.append(commands_item)

    result = doesCircleExist(commands)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
