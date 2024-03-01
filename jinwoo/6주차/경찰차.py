# m번 사건에서 n번 사건으로 이동하는 거리
def calc(m,n):
    ret= abs(li[m][0] - li[n][0])+abs(li[m][1] - li[n][1])

    return ret

# 두 경찰차가 각각 최근 m,n번째 사건을 해결했을 때 남은 사건의 이동거리의 최솟값
def solve(m,n):
    ret=0
    
    # 다음 사건
    next = max(m,n)+1
    
    # 다음 사건이없음
    if next == W+2:
        return 0
    
    if dp[m][n]!=-1:
        return dp[m][n]
    
    # 해당 사건을 첫 번째 or 두번째 경찰차가 해결
    calc1 = solve(next,n)+calc(m,next)
    calc2 = solve(m,next)+calc(n,next)
    if calc1 < calc2:
        dp_trace[m][n]=1
        dp[m][n]=calc1
    else :
        dp_trace[m][n]=2
        dp[m][n]=calc2
    ret = dp[m][n]
    
    return ret

N=int(input())
W =int(input())
li = [[1,1],[N,N]]
for _ in range(W):
    li.append(list(map(int,input().split())))
    

dp = [[-1]*1002 for _ in range(1002)]
dp_trace =[[-1]*1002 for _ in range(1002)]

print(solve(0,1))

## dp 역추적.
m,n = 0,1
for i in range(2,W+2):
    print(dp_trace[m][n])
    if dp_trace[m][n] ==1 :
        m=i
    else :
        n=iMOD = 1000000000

# n자리, k로 끝나는 계단 수의 개수
dp = [[-1]*11 for I in range(101)]

# 1자리 계단수.
dp[1][0]=0
for i in range(1,10):
  dp[1][i]=1
  
for i in range(2,101):
  dp[i][0] = dp[i-1][1]
  dp[i][9] = dp[i-1][8]
  for j in range(1,9):
    dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
    dp[i][j]%=MOD

n=int(input())
sum=0
for i in range(10):
  sum+=dp[n][i]
print(sum%MOD)