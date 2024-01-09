import math
import sys
sys.setrecursionlimit(10**6)

# cur에서 to발판으로 이동하는 힘 게산
def calcPower(cur,to):
    if to==0 : 
        return 0 ####
    elif cur==0 :
        return 2
    elif cur==to:
        return 1
    elif abs(cur-to)==2 :
        return 4
    return 3
    
# depth번째 발판, 왼발과 오른발이 l과 r에 위치할 때 부터 끝까지 힘의 최솟값
def solve(depth,l,r):
    
    #BaseCase
    if depth!=0 and arr[depth]==0:
        return 0
    
    if dp[depth][l][r]!=-1:
        return dp[depth][l][r]
    
    ret=float('inf')
    nextPos = arr[depth+1]
    
    # 왼발을 움직임
    ret=min(ret,solve(depth+1,nextPos,r)+calcPower(l,nextPos))
      
    # 오른발을 움직임 
    ret=min(ret,solve(depth+1,l,nextPos)+calcPower(r,nextPos))
    
    dp[depth][l][r] = ret
    return ret
    
arr = list(map(int,input().split()))
arr.insert(0,0)
n = len(arr)

dp = [[[-1,-1,-1,-1,-1] for i in range(5)] for _ in range(n)]

print(solve(0,0,0))

