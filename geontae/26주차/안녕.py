# dp[i][j] = 최대 체력이 j인 사람이 i번째 사람까지 진행했을 때의 최대 행복

n = int(input())
health = list(map(int, input().split()))
happy = list(map(int, input().split()))
dp = [[0] * 100 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(100):
        if health[i-1] <= j:
            dp[i][j] = max(happy[i-1] + dp[i-1][j-health[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][99])
