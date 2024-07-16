import sys

dy = [-1, 0, 1]
dx = [1, 1, 1]

def isRange(y, x, R, C):
    return 0 <= x < C and 0 <= y < R

def dfs(state, x, y):
    state[y][x] = 0

    if x == C - 1:
        return 1

    for i in range(3):
        nextY = y + dy[i]
        nextX = x + dx[i]

        if isRange(nextY, nextX, R, C) and state[nextY][nextX] == 1:
            ret = dfs(state, nextX, nextY)

            if ret == 1:
                return 1
            else:
                state[nextY][nextX] = 1

    return 0

def rollback(state, trace, y, x):
    while trace and trace[-1][1] >= x:
        t = trace.pop()

        pY = t[0]
        pX = t[1]

        state[pY][pX] = 1

def dfsStack(state, x, y):
    stack = [(y, x)]
    trace = []

    while stack:
        (y, x) = stack.pop()

        if x == C - 1:
            return 1

        state[y][x] = 0
        rollback(state, trace, y, x)

        trace.append((y, x))

        for i in range(2, -1, -1):
            nextY = y + dy[i]
            nextX = x + dx[i]

            if isRange(nextY, nextX, R, C) and state[nextY][nextX] == 1:
                stack.append((nextY, nextX))

    return 0

def sol(state):
    ret = 0

    for i in range(R):
        ret += dfsStack(state, 0, i)

    return ret

R, C = map(int, input().split(" "))
state = [[0 for j in range(C)] for i in range(R)]

for i in range(R):
    line = sys.stdin.readline()

    for j in range(C):
        if line[j] == 'x':
            state[i][j] = 0
        else:
            state[i][j] = 1

print(sol(state))