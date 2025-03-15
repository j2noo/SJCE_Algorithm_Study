# 40분

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
from collections import deque

arr = []
ans = 987654321


def cpy(arr):
    newArr = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            newArr[i][j] = arr[i][j]
    return newArr


for _ in range(5):
    arr.append(list(map(int, input().split())))
sr, sc = map(int, input().split())

queue = deque()
if arr[sr][sc] == 1:
    arr[sr][sc] = -1
    queue.append((sr, sc, cpy(arr), 1, 0))
else:
    arr[sr][sc] = -1
    queue.append((sr, sc, cpy(arr), 0, 0))

while len(queue) > 0:
    r, c, varr, cnt, moved = queue.popleft()
    if cnt == 3:
        ans = min(ans, moved)
        break

    for dir in range(4):
        newArr = cpy(varr)
        nr = r + dy[dir]
        nc = c + dx[dir]
        if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
            continue
        if newArr[nr][nc] == -1:  # 장애물
            continue
        if newArr[nr][nc] == 0:  # 사과X
            newArr[nr][nc] = -1  # 방문 처리
            queue.append((nr, nc, newArr, cnt, moved + 1))
        elif newArr[nr][nc] == 1:  # 사과 O
            newArr[nr][nc] = -1  # 방문 처리
            queue.append((nr, nc, newArr, cnt + 1, moved + 1))
if ans == 987654321:
    ans = -1
print(ans)