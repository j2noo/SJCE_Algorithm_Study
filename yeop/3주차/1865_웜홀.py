import sys

MAX = 10001
input = sys.stdin.readline

def bellman_ford(vertices, edges):
  n = len(vertices)
  dist = [MAX for _ in range(n)]
  
  for _ in range(n):
    for u, v, weight in edges:
      new_dist = dist[u] + weight
      if (new_dist < dist[v]):
        dist[v] = new_dist
        if (_ == n-1):
          return True
        
  return False

# 입력
TC = int(input())
for i in range(TC):
  N, M, W = map(int, input().split(' '))
  vertices = [i for _ in range(N+1)]
  edges = []
  
  for j in range(M):
    u, v, weight = map(int, input().split(' '))
    edges.append((u, v, weight))
    edges.append((v, u, weight))
  
  for j in range(W):
    u, v, weight = map(int, input().split(' '))
    edges.append((u, v, -weight))
  
  # sol
  flag = bellman_ford(vertices, edges)
  print('YES' if flag else 'NO')

  
  