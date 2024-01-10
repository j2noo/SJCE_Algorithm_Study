import sys
def sol(arr, n, m):
    ret = 0
    dp = [[0] * m for _ in range(n + 1)]

    for i in range(n):
        dp[i][0] = arr[i][0]
    for j in range(m):
        dp[0][j] = arr[0][j]

    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    for i in range(n):
        for j in range(m):
            ret = max(ret, dp[i][j])

    return ret ** 2

n, m = map(int, sys.stdin.readline().split(" "))
arr = [[] for _ in range(n)]

for i in range(n):
    s = sys.stdin.readline()
    arr[i] = list(map(int, s[:-1]))

print(sol(arr, n, m))