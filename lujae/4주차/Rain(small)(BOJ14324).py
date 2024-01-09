## 실패 ,,,
## maxupdated하다가 때려침

import copy
import sys

sys.setrecursionlimit(10**6)

dy = [-1, 0 , 1, 0]
dx = [0, -1, 0, 1]

def getBreakWaterPos(R, C):
    breakWaterPos = [[False] * C for _ in range(R)]

    for i in range(C):
        breakWaterPos[0][i] = True
        breakWaterPos[R - 1][i] = True

    for i in range(R):
        breakWaterPos[i][0] = True
        breakWaterPos[i][C - 1] = True

    return breakWaterPos

def rollback(updatedState, updatedList):
    for pos in updatedList:
        y = pos[0]
        x = pos[1]
        
        updatedState[y][x] = state[y][x]

def dfs(updatedState, breakWaterPos, visited, updatedList, maxUpdated, y, x):
    if breakWaterPos[y][x]:
        return 0

    visited[y][x] = True

    ret = 2000

    for i in range(4):
        nextY = y + dy[i]
        nextX = x + dx[i]

        if(updatedState[nextY][nextX] > updatedState[y][x]):
            ret = min(ret, updatedState[nextY][nextX])

        if not visited[nextY][nextX] and updatedState[y][x] >= updatedState[nextY][nextX]:
            ret = min(ret, dfs(updatedState, breakWaterPos, visited, updatedList, maxUpdated, nextY, nextX))

    if ret == 0:
        rollback(updatedState, updatedList)
    elif ret != 2000:
        if ret > updatedState[y][x]:
            updatedList.append((y, x))
            updatedState[y][x] = ret

    return updatedState[y][x]

def calDiff(state, updatedState, R, C):
    ret = 0

    print(state)
    print(updatedState)

    for i in range(R):
        for j in range(C):
            ret += updatedState[i][j] - state[i][j]

    return ret
def sol(state, R, C):
    breakWaterPos = getBreakWaterPos(R, C)
    updatedState = copy.deepcopy(state)

    for k in range(1000):
        visited = [[False] * C for _ in range(R)]

        for i in range(1, R - 1):
            for j in range(1, C - 1):
                if not breakWaterPos[i][j] and not visited[i][j]:
                    updatedList = []
                    dfs(updatedState, breakWaterPos, visited, updatedList, 0, i, j)

    return calDiff(state, updatedState, R, C)

T = int(input())
for t in range(T):
    R, C = map(int, sys.stdin.readline().split(" "))

    state = []
    for i in range(R):
        state.append(list(map(int, sys.stdin.readline().split(" "))))

    print("Case #%d: %d" %(t + 1, sol(state, R, C)))
