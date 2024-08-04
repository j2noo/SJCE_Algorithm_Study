# 시간: 12분
## DFS

import sys
sys.setrecursionlimit(10**6)

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def isRange(n, m, y, x):
    return 0 <= y < n and 0 <= x < m

def dfs(here, maps, visited, n, m):
    visited[here[0]][here[1]] = True

    ret = int(maps[here[0]][here[1]])

    for i in range(4):
        thereY = here[0] + dy[i]
        thereX = here[1] + dx[i]

        if isRange(n, m, thereY, thereX) and maps[thereY][thereX] != 'X' and not visited[thereY][thereX]:
            ret += dfs((thereY, thereX), maps, visited, n, m)

    return ret
def solution(maps):
    answer = []

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(dfs((i, j), maps, visited, n, m))

    if len(answer) == 0:
        return [-1]

    return sorted(answer)