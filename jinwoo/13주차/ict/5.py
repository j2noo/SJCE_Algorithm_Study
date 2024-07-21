#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'largestSubgrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY grid
#  2. INTEGER maxSum
#

# 2차원 부분합 트릭 + 이분탐색
# O(n*nlogn)
# psum[r][c] = A -b -d + D
def largestSubgrid(grid, maxSum):
    # Write your code here
    # print(grid_rows)
    print("!!",max(grid))
    psum = [[0]*(grid_rows+1) for _ in range(grid_rows+1)]
    
    for i in range(1,grid_rows+1):
        row_sum = 0
        for j in range(1,grid_rows+1):
            row_sum+= grid[i-1][j-1]
            if i==1:
                psum[i][j] = row_sum
            else :
                psum[i][j] = psum[i-1][j] + row_sum
            
    # for i in range(1,grid_rows+1):
    #     for j in range(1,grid_rows+1):
    #         print(psum[i][j],end="")
    #     print()
    
    ans=0
    # sze를 찾기위한 이분탐색
    # [lo.hi)
    lo = 1
    hi = grid_rows+1
    
    while( lo +1< hi):
        mid = (lo+hi)//2
        sze=mid
        
        # 결정문제  
        max_num_in_sze = -1
        for i in range(1,grid_rows+1-sze+1):
            for j in range(1,grid_rows+1-sze+1):
                if i+sze-1>grid_rows or j+sze-1>grid_rows :
                    continue
                sum1 = psum[i+sze-1][j+sze-1] - psum[i-1][j+sze-1] - psum[i+sze-1][j-1] + psum[i-1][j-1]
                max_num_in_sze = max(max_num_in_sze,sum1)
                
        print("lo,hi : ",lo,hi)
        print("sziee:",sze, "max() :",max_num_in_sze, "maxsum :", maxSum)
        print("---")

        if max_num_in_sze <= maxSum:
            lo = mid
        else :
            hi = mid
    print("lo,hi : ",lo,hi)
    
    # lo==1인 코너케이스에서, 0과 1을 구분해주는 과정
    if lo==1:
        mx = -1
        for i in range(1,grid_rows+1):
            for j in range(1,grid_rows+1):
               mx = max(mx,grid[i-1][j-1])
        print("lo : 1, mx,maxSum : ",mx,maxSum)
        if mx >  maxSum:
            return 0
        
        
    return lo
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    maxSum = int(input().strip())

    result = largestSubgrid(grid, maxSum)

    fptr.write(str(result) + '\n')

    fptr.close()
