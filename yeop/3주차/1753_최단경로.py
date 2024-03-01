import sys
import math
import heapq

INF = math.inf

def dijkstra(graph, start_vertex):
  lead_cost = [INF for _ in graph]
  
  lead_cost[start_vertex] = 0
  visited = set()
  heap = [] # 우선순위 큐, (cost, vertex)
  heapq.heappush(heap, (0, start_vertex))
  
  while heap:
    prev_cost, u = heapq.heappop(heap)
    
    if u in visited:
      continue
    visited.add(u)
    
    for v, weight in graph[u]:
      new_cost = prev_cost + weight
      if (new_cost < lead_cost[v]):
        lead_cost[v] = new_cost
        heapq.heappush(heap, (new_cost, v))
    
  return lead_cost

# 입력
V, E = map(int, sys.stdin.readline().split(' '))
graph = [[] for _ in range(V + 1)] # (v, weight)
start_vertex = int(sys.stdin.readline())
for _ in range(E):
  u, v, weight = map(int, sys.stdin.readline().split(' '))
  graph[u].append((v, weight))

lead_cost = dijkstra(graph, start_vertex)

# 출력
for vertex in range(1, V + 1):
  print(lead_cost[vertex] if lead_cost[vertex] != INF else 'INF')


