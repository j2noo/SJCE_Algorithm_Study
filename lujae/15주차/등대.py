# 시간: 30분
# dfs

import sys
sys.setrecursionlimit(10 ** 6)

# False 반환 안켜도 된다
# True 반환 켜야된다.
def dfs(adjList, here, visited, a):
    visited[here] = True

    ret = False
    for there in adjList[here]:
        if not visited[there]:
            ret |= not dfs(adjList, there, visited, a)

    if ret == True:
        a[0] += 1

    return ret

def solution(n, lighthouse):
    adjList = [[] for i in range(n + 1)]

    a = [0]
    for e in lighthouse:
        adjList[e[0]].append(e[1])
        adjList[e[1]].append(e[0])

    dfs(adjList, 1, [False] * (n + 1), a)
    return a[0]

print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))