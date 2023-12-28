import sys

def printDist(dist, N):
    ret = ""
    num = 0

    for i in range(2, N + 1):
        num = dist[i]
        if num == float("inf"):
            num = -1

        ret += str(num) + "\n"

    print(ret)

def bellman_ford(adj, N):
    dist = [float("inf") for _ in range(N+1)]
    dist[1] = 0
    nCycle = False

    for i in range(N):
        nCycle = False

        for here in range(1, N + 1):
            if(dist[here] != float("inf")):
                for there, weight in adj[here]:
                    if(dist[there] > dist[here] + weight):
                        dist[there] = dist[here] + weight
                        nCycle = True

    if(nCycle):
        print(-1)
        return
    else:
        printDist(dist, N)


def readIntegers():
    return map(int, sys.stdin.readline().split(" "))

N, M = readIntegers()
adj = [[] for _ in range(N + 1)]

for i in range(M):
    A, B, C = readIntegers()

    adj[A].append((B, C))

bellman_ford(adj, N)