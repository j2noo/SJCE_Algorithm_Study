# 14qns
import sys
sys.setrecursionlimit(int(1e7))
# x를 y로 변환
INF = 987654321
dp = [-1]*1_000_001

def dfs(x,y,n):
    if x > y :
        return INF
    if x==y :
        return 0
    if dp[x]!=-1:
        return dp[x]
    
    ret = INF
    ret = min(ret,dfs(x+n,y,n)+1)
    ret = min(ret,dfs(x*2,y,n)+1)
    ret = min(ret,dfs(x*3,y,n)+1)
    dp[x]=ret
    return ret
    
def solution(x, y, n):
    answer = dfs(x,y,n)
    if answer == INF:
        answer = -1
    return answer

# dfs + dp