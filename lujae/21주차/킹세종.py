import sys
import collections

def bfs(adj, start, n):
    ret = dict()
    INF = 987654321

    deque = collections.deque()
    discovered = [False] * (n + 1)

    deque.append((start, 0))
    discovered[start] = True

    while deque:
        (here, d) = deque.popleft()

        if d != 0 and d not in ret:
            ret[d] = set()
        if d in ret:
            ret[d].add(here)

        for there in adj[here]:
            if not discovered[there]:
                discovered[there] = True
                deque.append((there, d + 1))

    for i in range(1, n + 1):
        if not discovered[i]:
            ret[INF].add(i)

    return  ret

def solve(adj, n, edge_dic):
    group_distance_with_1 = bfs(adj, 1, n)
    group_distance_with_2 = bfs(adj, 2, n)

    INF = 987654321

    ret = 0
    while True:
        update_flag = False

        for d1 in group_distance_with_1:
            for d2 in group_distance_with_2:


    return ret



n, m = map(int, input().split())

adj = [[] for i in range(n + 1)]

edge_dic = {}
for i in range(m):
    u, v = map(int, sys.stdin.readline().split(" "))

    min_vertex = min(u, v)
    max_vertex = max(u, v)
    edge_dic[(min_vertex, max_vertex)] = True

    adj[u].append(v)
    adj[v].append(u)

solve(adj, n)

