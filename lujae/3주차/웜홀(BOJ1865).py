import sys

def bellman_ford(adj, N):
    upper = [987654321] * (N + 1)
    nCycle = False

    for i in range(N):
        nCycle = False

        for here in range(1, N + 1):
            for there, weight in adj[here]:
                if(upper[there] > upper[here] + weight):
                    upper[there] = upper[here] + weight
                    nCycle = True

    if(nCycle):
        print("YES")
    else:
        print("NO")

def readIntegers():
    return map(int, sys.stdin.readline().split(" "))

TC = int(input())

for i in range(TC):
    N, M, W = readIntegers()
    adj = [[] for _ in range(N + 1)]

    for j in range(M):
        S, E, T = readIntegers()
        adj[S].append((E, T))
        adj[E].append((S, T))

    for j in range(W):
        S, E, T = readIntegers()
        adj[S].append((E, -T))

    bellman_ford(adj, N)