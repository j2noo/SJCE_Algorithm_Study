import sys
import heapq
def dijkstra(edge, V, K):
    dist = [sys.maxsize] * (V + 1)
    dist[K] = 0
    pq = []
    pq.append((0, K))

    while(pq):
        cost, here = heapq.heappop(pq)

        if dist[here] < cost:
            continue

        for (there, weight) in edge[here]:
            if(dist[there] > dist[here] + weight):
                dist[there] = dist[here] + weight
                heapq.heappush(pq, (dist[there], there))

    return dist

def printDist(dist, V, K):
    num = 0
    ret = ""

    for i in range(1, V + 1):
        if(i == K): num = 0
        else: num = dist[i]

        if(num == sys.maxsize):
            num = "INF"

        ret += str(num) + "\n"

    print(ret)


V,E = map(int, input().split(" "))

K = int(input())

edge = [[] for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split(" "))
    edge[u].append((v, w))

printDist(dijkstra(edge, V, K), V, K)