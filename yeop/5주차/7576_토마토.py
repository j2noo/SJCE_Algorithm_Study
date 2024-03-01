import sys
from collections import deque

input = sys.stdin.readline
# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# N: 열
# M: 행
tomatoes = []
queue = []
day = 0

def check_index(x, y, max_x, max_y):
  return 0 <= x < max_x and 0 <= y < max_y

def bfs(tomatoes, queue):
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if (check_index(nx, ny, M, N) and tomatoes[nx][ny] == 0):
        tomatoes[nx][ny] = tomatoes[x][y] + 1
        queue.append([nx, ny])
    
  return tomatoes
        
def sol(tomatoes):
  queue = deque([])
  for i in range(M):
    for j in range(N):
      if (tomatoes[i][j] == 1):
        queue.append([i, j])
  
  after_tomatoes = bfs(tomatoes, queue)
  
  for i in range(M):
    for j in range(N):
      if (tomatoes[i][j] == 0):
        return -1
  
  return max(max(row) for row in after_tomatoes) - 1
  

# 입력
N, M = list(map(int, input().split()))
for _ in range(M):
  row = list(map(int, input().split()))
  tomatoes.append(row)
  
print(sol(tomatoes))