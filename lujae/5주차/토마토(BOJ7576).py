import sys
import collections
#최단 경로 문제

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def isRange(y, x):
    return 0 <= y < N and 0 <= x < M

def checkState():
    for i in range(N):
        for j in range(M):
            if state[i][j] == 0:
                return False;

    return True
def sol():
    if checkState():
        return 0
    INF = 987654321
    q = collections.deque()
    days = [[-1] * M for i in range(N)]

    for i in range(N):
        for j in range(M):
            if state[i][j] == 1:
                q.append((i, j, 0))
                days[i][j] = 0

    while q:
        y, x, day = q.popleft()

        for i in range(4):
            nextY = y + dy[i]
            nextX = x + dx[i]

            if isRange(nextY, nextX) and state[nextY][nextX] == 0:
                state[nextY][nextX] = 1
                days[nextY][nextX] = day + 1
                q.append((nextY, nextX, day + 1))

    if not checkState():
        return -1
    else:
        return max(max(r) for r in days)

M, N = map(int, sys.stdin.readline().split(" "))
state = []
for i in range(N):
    state.append(list(map(int, sys.stdin.readline().split(" "))))

print(sol())