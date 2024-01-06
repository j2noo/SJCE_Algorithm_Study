from collections import deque

n = int(input())
array = []
max_height = 1
result = 1
for _ in range(n):
    li = list(map(int,input().split()))
    if max_height < max(li):
        max_height = max(li)
    array.append(li)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(temp_array, queue, height):
    while queue:
        x, y = queue.popleft()

        for c in range(4):
            next_i = x + dx[c]
            next_j = y + dy[c]

            if 0 <= next_i < n and 0 <= next_j < n:
                # 방문한 곳은 0으로 만들기 때문에 따로 방문 체크 필요 x
                if temp_array[next_i][next_j] > height:
                    queue.append((next_i, next_j))
                    temp_array[next_i][next_j] = 0
    return temp_array


for height in range(1, max_height):
    temp_array = [arr[:] for arr in array]
    queue = deque()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if temp_array[i][j] > height:
                temp_array[i][j] = 0
                queue.append((i,j))
                temp_array = bfs(temp_array, queue, height)
                cnt += 1

    if cnt > result:
        result = cnt

print(result)