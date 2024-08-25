# 시간 10분
# DP

def solution(x, y, n):
    INF = 987654321
    dp = [INF] * (y + 1)

    dp[x] = 0

    for i in range(x, y + 1):
        dp[i] = min(dp[i], dp[i - n] + 1)

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    if dp[y] == INF:
        return -1
    return dp[y]