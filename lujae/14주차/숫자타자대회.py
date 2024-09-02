def isRange(y, x, n, m):
    return 0 <= y < n and 0 <= x < m


def getMinCostMap():
    dist = [[float('inf')] * 10 for _ in range(10)]

    for i in range(10):
        dist[i][i] = 1

    dy = [-1, 0, 1, 0, -1, -1, 1, 1]
    dx = [0, -1, 0, 1, 1, -1, -1, 1]
    cost = [2] * 4 + [3] * 4

    for y in range(3):
        for x in range(3):
            for dI in range(8):
                ty = y + dy[dI]
                tx = x + dx[dI]
                if isRange(ty, tx, 3, 3):
                    dist[y * 3 + x][ty * 3 + tx] = cost[dI]
                    dist[ty * 3 + tx][y * 3 + x] = cost[dI]

    for i in range(6, 9):
        dist[9][i] = 3
        dist[i][9] = 3

    dist[9][7] = 2
    dist[7][9] = 2

    for k in range(10):
        for i in range(10):
            for j in range(10):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def solution(numbers):
    INF = float('inf')
    dp = [[[INF] * 10 for _ in range(10)] for _ in range(len(numbers))]

    numpad = [
        '1', '2', '3',
        '4', '5', '6',
        '7', '8', '9',
        '0'
    ]

    idxDic = {numpad[i]: i for i in range(10)}
    costMap = getMinCostMap()

    leftPos = idxDic['4']
    rightPos = idxDic['6']

    dp[0][idxDic[numbers[0]]][rightPos] = costMap[leftPos][idxDic[numbers[0]]]
    dp[0][leftPos][idxDic[numbers[0]]] = costMap[rightPos][idxDic[numbers[0]]]

    for i in range(1, len(numbers)):
        num = idxDic[numbers[i]]
        for j in range(10):
            for k in range(10):
                if j != k:
                    dp[i][num][k] = min(dp[i][num][k], dp[i - 1][j][k] + costMap[j][num])
                    dp[i][j][num] = min(dp[i][j][num], dp[i - 1][j][k] + costMap[k][num])

    answer = min(min(dp[len(numbers) - 1][i][j] for i in range(10)) for j in range(10))

    return answer