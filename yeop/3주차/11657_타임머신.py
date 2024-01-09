import sys
import math

INF = math.inf
input = sys.stdin.readline

def bellman_ford(V, E, start_vertex):
  dist = [INF for _ in V]
  dist[start_vertex] = 0
  exist_minus_cycle = False
  
  N = len(V)
  
  for i in range(N):
    for u, v, weight in E:
      if dist[u] == INF:
        continue
      
      new_weight = dist[u] + weight
      if new_weight < dist[v]:
        dist[v] = new_weight
        if i == N - 1:
          exist_minus_cycle = True
  
  return dist, exist_minus_cycle

# 입력
N, M = map(int, input().split(' '))
V = [i for i in range(N+1)]
E = []
for _ in range(M):
  u, v, weight = map(int, input().split(' '))
  E.append((u, v, weight))
  
# 출력
dist, flag = bellman_ford(V, E, 1)
if flag == True:
  print(-1)
else:
  for i in range(2, N+1):
    print(dist[i] if dist[i] != INF else -1)