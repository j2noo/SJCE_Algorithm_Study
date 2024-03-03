from collections import deque
m, n = map(int, input().split())
arr = []
queue = deque()

# 입력받으면서 첫날 바뀔 애들을 큐에 넣기
for i in range(n):
    a = list(map(int, input().split()))
    for j, x in enumerate(a):
        if x == 1:
            queue.append([i, j])
    arr.append(a)
# 오늘과 내일의 경계는 -1로 표기
queue.append([-1, -1])

dx = [1,0,-1,0]
dy = [0,1,0,-1]
day = 0

while queue:
    i, j = queue.popleft()
    # 하루가 지났다는 뜻
    if i == -1:
        # 바뀔 애들이 있다면
        if queue:
            queue.append([-1, -1])
            day += 1
        # 바뀔 애들이 없다면
        else:
            break
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1
                # 바뀔 애들 추가
                queue.append([nx, ny])

f = 0
for i in range(n):
    if 0 in arr[i]:
        f = 1
if f:
    print(-1)
else:
    print(day)



