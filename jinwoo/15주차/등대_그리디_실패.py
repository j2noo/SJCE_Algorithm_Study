import sys
from collections import deque
sys.setrecursionlimit(int(1e7))

def solution(n, lighthouse):
    # 자식 노드를 탐색하는 함수
    def dfs(v,parent):
        parents[v] = parent
        for incident in graph[v]:
            if incident == parent:
                continue
            dfs(incident,v)
        # 리프노드    
        if len(graph[v])==1 and v!=1: # 이세끼
            leafs.append(v)
        
    graph = [[] for _ in range(n+1)]
    parents = [-1]*(n+1)
    leafs = []
    
    for s,e in lighthouse:
        graph[s].append(e)
        graph[e].append(s)
    
    # root의 부모는 -1번
    root=1
    dfs(root,-1)
    
    # print('parents : ',parents)
    # print('leafs : ',leafs)
    
    ## bfs
    on = [-1] * (n+1)
    visited = [-1] * (n+1)
    queue = deque()
    
    # 리프노드 부모는 다 켜기
    for leaf in leafs:
        parent = parents[leaf]
        on[parent]=1
        if visited[parent] == -1:
            queue.append(parent)
            visited[parent]=1
            
        
    # 큐 순회하면서, 내가 켜져있으면 무시하고 부모 append
    # 큐 순회하면서, 내가 꺼져있으면 부모를 켬
    while(len(queue)>0):
        v = queue.popleft()
        if v==1:
            continue
            
        parent = parents[v]
        # 내가 꺼져있으면 부모를 무조건 켜야함
        if on[v]==-1:
            on[parent]=1
            
        # 내가 켜져있음 -> 노상관
        # print(f'{v}의 부모 : {parents[v]}')
        if visited[parent]==-1:
            queue.append(parent)
            visited[parent]=1

    if on[0]==1:
        for i in range(13333333):
            print("!@#@!#")
    return on.count(1)

# 차수가 제일 높은 등대 켜기 x
# 리프노드의 부모는 무조건 켜기
# v를 이용한 bfs, 내가 꺼져있으면 부모는 켜기, 내가 켜져있으면 부모는 상관x