n = int(input())
visitedNode = []
map = [list(map(int, input())) for _ in range(n)]
cnt = []


def dfs(i, j, visitedNode):
    visitedNode.append([i, j])
    if i < n-1 and map[i+1][j] == 1:
        if [i+1, j] not in visitedNode:
            dfs(i+1, j, visitedNode)

    if i > 0 and map[i-1][j] == 1:
        if [i-1, j] not in visitedNode:
            dfs(i-1, j, visitedNode)

    if j < n-1 and map[i][j+1] == 1:
        if [i, j+1] not in visitedNode:
            dfs(i, j+1, visitedNode)

    if j > 0 and map[i][j-1] == 1:
        if [i, j-1] not in visitedNode:
            dfs(i, j-1, visitedNode)

    return visitedNode


# print(dfs(0, 4, visitedNode))

for i in range(0, n):
    for j in range(0, n):
        if map[i][j] == 1:
            if [i, j] not in visitedNode:
                visited = []
                tcnt = dfs(i, j, visited)
                visitedNode.extend(tcnt)
                cnt.append(len(tcnt))
cnt.sort()
print(len(cnt))
for i in range(0, len(cnt)):
    print(cnt[i])
