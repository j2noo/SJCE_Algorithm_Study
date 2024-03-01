import sys
sys.setrecursionlimit(10**6)

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def isRange(n, m, y, x):
    return 0 <= y and y < n and 0 <= x and x < m
def dfs(currentY, currentX, visited, rain):
    visited[currentY][currentX] = True

    for i in range(4):
        nextY = currentY + dy[i]
        nextX = currentX + dx[i]

        if isRange(N, N, nextY, nextX) and not visited[nextY][nextX]:
            if arr[nextY][nextX] > rain:
                dfs(nextY, nextX, visited, rain)
def sol():
    ret = 1
    for rain in range(100, 0, -1):
        visited = [[False] * N for _ in range(N)]

        cntArea = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and arr[i][j] > rain:
                    dfs(i, j, visited, rain)
                    cntArea += 1

        ret = max(ret, cntArea)

    return ret

N = int(input())
arr = []

for i in range(N):
    li = list(map(int, sys.stdin.readline().split(" ")))
    arr.append(li)

print(sol())