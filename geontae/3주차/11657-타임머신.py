import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))


def bellman_ford(start):
    i = start
    for _ in range(N):
        for node, w in graph[i]:
            # dist[i] != INF 조건 추가해야 합격
            if dist[i] != INF and dist[i] + w < dist[node]:
                dist[node] = dist[i] + w
        if i < N:
            i += 1
        else:
            i = 1


dist[1] = 0

for i in range(1,N+1):
    bellman_ford(i)

tempDist = dist.copy()
bellman_ford(1)
isCycle = dist != tempDist


if not isCycle:
    for i in range(2, N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)