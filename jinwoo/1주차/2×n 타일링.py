n = int(input())
MOD = 10007
dp = [-1] * 1010

dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= MOD
print(dp[n])
