# 완탐 : 1000C30
# dp[현재초][자두위치][남은횟수] 최대

INF = float("inf")
T,W = map(int,input().split())
times = []
dp = [[[-1]*(W+1) for _ in range(2)] for _ in range(T+1)]

for _ in range(T):
    times.append(int(input()))

# second초에, pos위치에 있고 남은 횟수가 left일때 자두 개수의 최댓값
def solve(second, pos, left):
    if second == T :
        return 0
    
    if dp[second][pos][left] != -1 :
        return dp[second][pos][left]
    
    ret = -INF
    
    if times[second] == pos + 1:  # 자두가 있음
        isPlum = 1
    else:
        isPlum = 0
    
    # 움직임
    if left>0: 
        ret = max(ret,solve(second+1, (pos+1)%2, left-1) + isPlum)
    
    # 안움직임
    ret = max(ret,solve(second+1, pos, left) + isPlum)
    dp[second][pos][left] = ret
    # print(f'second, pos, left {second,pos,left} : {ret}')

    return ret


ans = max(solve(0,0,W), solve(0,1,W-1))
print(ans)