def calPower(start, end):
    distance = abs(end - start)

    if(start == 0):
        return 2
    if(distance == 2):
        return 4
    if(start == end):
        return 1

    return 3

def sol(arr):
    if(len(arr) - 1 == 1):
        return 2

    INF = 99999999
    ret = INF
    dp = [[[INF] * 5 for _ in range(5)] for i in range(len(arr))]


    dp[0][0][arr[0]] = 2
    dp[0][arr[0]][0] = 2

    for i in range(1, len(arr) - 1):
        for j in range(5):
            for k in range(5):
                dp[i][j][arr[i]] = min(dp[i][j][arr[i]], dp[i - 1][j][k] + calPower(k, arr[i]))
                dp[i][arr[i]][j] = min(dp[i][arr[i]][j], dp[i - 1][k][j] + calPower(k, arr[i]))

    for i in range(5):
        for j in range(5):
            ret = min(ret, dp[len(arr) - 2][i][j])

    return ret;

arr = list(map(int, input().split()))

print(sol(arr))