N = int(input())
graph = []
result = []

for _ in range (N):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0

def dfs(x, y):
    global count

    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for x in range (N):
    for y in range (N):
        if graph[x][y] == 1:
            dfs(x, y)
            result.append(count)
            count = 0

result.sort()
print(len(result))
for i in result:
    print(i)