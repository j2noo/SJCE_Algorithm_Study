import copy
import sys
from collections import deque

dy = [-1, 0 , 1, 0]
dx = [0, -1, 0, 1]

def isRange(R, C , y, x):
    return 0 <= y < R and 0 <= x < C

def isBoundary(R, C, y, x):
    return y == 0 or y == R - 1 or x == 0 or x == C - 1

def bfs(state, updatedState, startY, startX):
    visited = [[False] * C for _ in range(R)]

    queue = deque()
    queue.append((startY, startX))
    visited[startY][startX] = True

    trace = []
    wallHeight = 987654321

    while queue:
        (hereY, hereX) = queue.pop()

        if not isBoundary(R, C, hereY, hereX):
            trace.append((hereY, hereX))

        for i in range(4):
            thereY = hereY + dy[i]
            thereX = hereX + dx[i]

            if(not isRange(R, C, thereY, thereX)):
                wallHeight = 0
            else:
                if not visited[thereY][thereX] and state[thereY][thereX] > state[hereY][hereX]:
                    wallHeight = min(wallHeight, state[thereY][thereX])

                if not visited[thereY][thereX] and state[hereY][hereX] >= state[thereY][thereX]:
                    visited[thereY][thereX] = True
                    queue.append((thereY, thereX))

    for (y, x) in trace:
        if wallHeight > state[y][x]:
            updatedState[y][x] = wallHeight

def calDiff(state, updatedState, R, C):
    ret = 0

    for i in range(R):
        for j in range(C):
            ret += updatedState[i][j] - state[i][j]

    return ret
def sol(state, R, C):
    initState = copy.deepcopy(state)
    updatedState = copy.deepcopy(state)

    for i in range(1, R):
        for j in range(1, C):
                bfs(state, updatedState, i, j)
                state = copy.deepcopy(updatedState)

    return calDiff(initState, updatedState, R, C)

T = int(input())
for t in range(T):
    R, C = map(int, sys.stdin.readline().split(" "))

    state = []
    for i in range(R):
        state.append(list(map(int, sys.stdin.readline().split(" "))))

    print("Case #%d: %d" %(t + 1, sol(state, R, C)))