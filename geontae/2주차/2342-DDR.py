import sys
sys.setrecursionlimit(10**6)

arr = list(map(int, sys.stdin.readline().split()))


def checkWeight(s, d):
    if s == d:
        return 1
    if s == 0:
        return 2
    if abs(s-d) == 1 or abs(s-d) == 3:
        return 3
    if abs(s-d) == 2:
        return 4


def solve(n, left, right):
    if n >= len(arr)-1:
        return 0
    if dp[n][left][right] != -1:
        return dp[n][left][right]
    dp[n][left][right] = min(solve(n+1, arr[n], right) + checkWeight(
        left, arr[n]), solve(n+1, left, arr[n]) + checkWeight(right, arr[n]))

    return dp[n][left][right]


n = len(arr)
dp = [[[-1]*5 for _ in range(5)] for _ in range(n)]
# solve(0, 0, 0)
print(solve(0, 0, 0))
