MOD = 1000000000

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