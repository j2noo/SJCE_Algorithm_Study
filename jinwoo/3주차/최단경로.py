def dijk():
    visited[start]=1
    
    for node in adj[start]:
        print(node)

V, E = map(int,input().split())
start = int(input())
adj = [[] for _ in range(V+1)] 
visited = [0 for i in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    adj[u].append([v,w])
    # adj[v].append([u,w])...
print(adj)

dijk()

