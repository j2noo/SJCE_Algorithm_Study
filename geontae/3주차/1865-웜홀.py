import sys

input = sys.stdin.readline

TC = int(input())
INF = sys.maxsize
result = [False] * TC


def bellman_ford(N):
    dist = [INF] * (N + 1)
    dist[1] = 0
    for j in range(N):
        for i in range(1, N+1):
            for node, w in graph[i]:
                if dist[i] + w < dist[node]:
                    dist[node] = dist[i] + w
                    if j == N-1:
                        return True
    return False


for i in range(0, TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))

    result[i] = bellman_ford(N)


for r in result:
    if r:
        print("YES")
    else:
        print("NO")

