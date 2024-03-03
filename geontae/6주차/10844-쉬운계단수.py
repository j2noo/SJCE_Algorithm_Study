n = int(input())
cnt = 0
# dp[i][j] = i번째에서 끝자리가 j로 끝나는 경우의 수
dp = [[1]*10 for _ in range(n+1)]
dp[1][0] = 0

for i in range(2, n+1):
    for j in range(0,10):
        if j == 0:
            dp[i][j] = (dp[i-1][1]) % 1000000000
        elif j == 9:
            dp[i][j] = (dp[i-1][8]) % 1000000000
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000

print(sum(dp[n]) % 1000000000)