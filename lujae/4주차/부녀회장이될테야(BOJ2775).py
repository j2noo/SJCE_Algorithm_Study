import sys

def accumulatePeople(dp, y, x):
    ret = 0
    for j in range(1, x + 1):
            ret += dp[y - 1][j]

    return ret

T = int(input())

dp = [[0] * 15 for _ in range(15)]
for i in range(1, 15):
    dp[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = accumulatePeople(dp, i, j)

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    print(dp[k][n])
