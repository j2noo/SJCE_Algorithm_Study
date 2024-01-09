from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]


total = 0
sumArr = []


# -- bfs를 이용한 풀이--
def bfs(r, c):
    depth = 0  # 여기서는 안쓰임
    sum = 0
    queue = deque()
    queue.append([r, c])
    visited[r][c] = 1
    while len(queue) > 0:
        depth += 1
        qSize = len(queue)
        for i in range(qSize):
            pop = queue.popleft()
            sum += 1
            for j in range(4):
                nr = pop[0] + dy[j]
                nc = pop[1] + dx[j]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if visited[nr][nc] == 0 and arr[nr][nc] == 1:
                    queue.append([nr, nc])
                    visited[nr][nc] = 1  # 안해주면 무한루프!!
    return sum


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and arr[i][j] == 1:
            sumArr.append(bfs(i, j))
            total += 1

print(total)
sumArr.sort()
for i in sumArr:
    print(i)


# -- bfs를 이용한 풀이--


# -- dfs를 이용한 풀이--
# def dfs(r, c):
#     sum = 1
#     visited[r][c] = 1
#     for i in range(4):
#         nr = r + dy[i]
#         nc = c + dx[i]
#         if nr < 0 or nr >= N or nc < 0 or nc >= N:
#             continue
#         if visited[nr][nc] == 0 and arr[nr][nc] == 1:
#             sum += dfs(nr, nc)
#     return sum


# for i in range(N):
#     for j in range(N):
#         if visited[i][j] == 0 and arr[i][j] == 1:
#             sumArr.append(dfs(i, j))
#             total += 1

# print(total)
# sumArr.sort()
# for i in sumArr:
#     print(i)
# -- dfs를 이용한 풀이--


# list의 append,pop은 O(N)이므로 사용하지 말것
