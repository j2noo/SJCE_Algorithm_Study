import sys
sys.setrecursionlimit(10 ** 6)

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def isRange(R, C, y, x):
    return 0 <= y < R and 0 <= x < C

def checkLevel(R, C, level, state, waterSurface):
    for i in range(0, R):
        for j in range(0, C):
            if state[i][j] < level:
                waterSurface[i][j] = True

def dfs(R, C, visited, state, waterSurface, hereY, hereX, level):
    visited[hereY][hereX] = True
    waterSurface[hereY][hereX] = False

    for i in range(4):
        thereY = hereY + dy[i]
        thereX = hereX + dx[i]

        if isRange(R, C, thereY, thereX) and not visited[thereY][thereX] and level > state[thereY][thereX]:
            dfs(R, C, visited, state, waterSurface, thereY, thereX, level)
def excludeWater(R, C, state, waterSurface, level):
    visited = [[False] * C for _ in range(R)]

    for i in range(R):
        if waterSurface[i][0]:
            dfs(R, C, visited, state, waterSurface, i, 0, level)
        if waterSurface[i][C - 1]:
            dfs(R, C, visited, state, waterSurface, i, C - 1, level)

    for j in range(C):
        if waterSurface[0][j]:
            dfs(R, C, visited, state, waterSurface, 0, j, level)
        if waterSurface[R - 1][j]:
            dfs(R, C, visited, state, waterSurface, R - 1, j, level)

def calWater(R, C, waterSurface):
    ret = 0

    for i in range(1, R):
        for j in range(1, C):
            if waterSurface[i][j]: ret += 1

    return ret

def sol(state, R, C):
    ret = 0;
    maxHeight = max(e for r in state for e in r)
    waterSurface = [[False] * C for _ in range(R)]

    for level in range(1, maxHeight + 1):
        checkLevel(R, C, level, state, waterSurface)
        excludeWater(R, C, state, waterSurface, level)
        ret += calWater(R, C, waterSurface)

    return ret

T = int(input())
for t in range(T):
    R, C = map(int, sys.stdin.readline().split(" "))

    state = []
    for i in range(R):
        state.append(list(map(int, sys.stdin.readline().split(" "))))

    print("Case #%d: %d" % (t + 1, sol(state, R, C)))