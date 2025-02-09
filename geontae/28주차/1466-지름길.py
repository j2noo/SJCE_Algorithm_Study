# dp[i] = i번째까지 올 수 있는 최소 거리
# dp[i] = min(dp[start] + cost, dp[i-1] + 1)
n, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(d+1)
for i in range(1, d+1):
    dp[i] = dp[i-1] + 1
    for j in range(n):
        start, end, cost = arr[j]
        if end == i:
            dp[i] = min(dp[start] + cost, dp[i])

print(dp[d])
