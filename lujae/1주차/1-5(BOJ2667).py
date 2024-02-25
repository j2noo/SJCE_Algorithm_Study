import sys

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def isRange(y, x, N):
    return 0 <= x < N and 0 <= y < N

def dfs(state, y, x, N):
    state[y][x] = 0

    ret = 1

    for i in range(4):
        nextY = y + dy[i]
        nextX = x + dx[i]

        if(isRange(nextY, nextX, N) and state[nextY][nextX] == 1):
            ret += dfs(state, nextY, nextX, N)

    return ret

def sol(state, N):
    cntComplex = []

    for i in range(N):
        for j in range(N):
            if(state[i][j] == 1):
                cntComplex.append(dfs(state, i, j, N))

    return sorted(cntComplex)

N = int(input())

stateStr = [sys.stdin.readline() for _ in range(N)]
state = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        if(stateStr[i][j] == '1'):
            state[i][j] = 1

cntComplex = sol(state, N)
print(len(cntComplex))
for cnt in cntComplex:
    print(cnt)
