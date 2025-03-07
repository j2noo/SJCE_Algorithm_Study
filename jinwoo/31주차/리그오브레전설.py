# 10000 C 5000 완탐X
# dp[n] : n초일떄 경우의 수
# ABA -> AABA and BABA
# dp[n] = dp[n-1] + dp[n-B]

MOD = 1_000_000_007
N,M = map(int,input().split())
dp = [-1]*10001

dp[1] = 1 # 1초
dp[2] = 1 # 2초

# M초 이전까지는 1가지
for i in range(1,M) :
    dp[i] = 1
dp[M] = 2

for i in range(M+1,N+1):
    dp[i] = (dp[i-1] + dp[i-M]) % MOD
# print(dp)
print(dp[N] % 1_000_000_007)