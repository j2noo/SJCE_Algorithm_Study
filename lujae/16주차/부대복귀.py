## 40분
## dstination에서 BFS
import collections

def bfs(adj, n, start):
    INF = 987654321
    dist = [INF] * (n + 1)

    dist[start] = 0
    dq = collections.deque()
    dq.append((0, start))

    while dq:
        cost, here = dq.popleft()

        for there in adj[here]:
            if dist[there] == INF:
                dist[there] = cost + 1
                dq.append((dist[there], there))

    return dist

def solution(n, roads, sources, destination):
    answer = []
    INF = 987654321
    adj = [[] for i in range(n + 1)]

    for r in roads:
        adj[r[0]].append(r[1])
        adj[r[1]].append(r[0])

    dist = bfs(adj, n, destination)
    for s in sources:
        cost = dist[s]
        if cost == INF:
            answer.append(-1)
        else:
            answer.append(cost)

    return answer

solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5)