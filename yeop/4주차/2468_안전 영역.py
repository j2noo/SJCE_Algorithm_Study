import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 입력
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def check_index(i, j, n, m):
  return 0 <= i < n and 0 <= j < m

def dfs(x, y, N):
  if (matrix[y][x] < 0 or marked[y][x] == 1):
    return 0
  
  marked[y][x] = 1 # 마킹
  
  for k in range(4):
    # 상하좌우 탐색
    nx = x + dx[k]
    ny = y + dy[k]
    if (check_index(nx, ny, N, N)):
      dfs(nx, ny, N)
  
  return 1
      
    

rain = 1
max_safe = 0
for _ in range(100):
  marked = [[0] * N for _ in range(N)]
  count = 0
  
  # 1씩 깎기
  for i in range(N):
    for j in range(N):
      matrix[i][j] -= 1
      
  # 조사
  for i in range(N):
    for j in range(N):
      flag = dfs(j, i, N)
      if (flag):
        count += 1
  
  if (count == 0):
    break
  if (max_safe < count):
    max_safe = count    
  
# 답
print(max_safe)