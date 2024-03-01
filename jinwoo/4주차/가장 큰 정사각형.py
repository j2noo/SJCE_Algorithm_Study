# r,c를 죄상단으로 가지는 가장 큰 정사각형의 한 변 길이
def solve(r,c):
    global ans
    if r>=n or c>=m :
        return 0
    if dp[r][c][2]!=-1:
        return dp[r][c][2]
        
    ret=0
    ret=min(dp[r][c][0],dp[r][c][1],solve(r+1,c+1)+1)
    dp[r][c][2]=ret
    
    ans=max(ans,ret)
    return ret
    
n,m = map(int,input().split())
arr = list(list(map(int,input())) for _ in range(n))
ans=0

# dp 경계값 예외 처리 위해 범위 크게 잡고, 0으로 초기화
dp = [[[0,0,-1] for _ in range(m+1)] for _ in range(n+1)]


# dp(i,j,0) : 가로로 최대 길이 계산
for i in range(n):
    for j in range(m-1, -1, -1):
        if arr[i][j]==0:
            dp[i][j][0]=0
        else:
            dp[i][j][0]= 1 + dp[i][j+1][0] 
            
# dp(i,j,1) : 세로로 최대 길이 계산
for j in range(m):
    for i in range(n-1,-1,-1):
        if arr[i][j]==0:
            dp[i][j][1]=0
        else:
            dp[i][j][1]= 1 + dp[i+1][j][1]
            
for i in range(n):
    for j in range(m):
        solve(i,j)
        
print(ans**2)