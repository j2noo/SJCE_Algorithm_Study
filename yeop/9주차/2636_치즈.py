import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 입력
height, width = map(int, input().split())
square = []
for _ in range(height):
  row = list(map(int, input().split()))
  square.append(row)


def dfs(i, j, c_list, visited):
  # 1. 인덱스 검사
  if not (0 <= i < height and 0 <= j < width and visited[i][j] == False):
    return
  
  visited[i][j] = True
  # 2-1. 0일 시 상하좌우 검사
  if square[i][j] == 0:
    for k in range(4):
      dfs(i + dy[k], j + dx[k], c_list, visited)
  # 2-2. 아닐 시 c 목록에 추가
  else:
    c_list.add((i, j))
    

# 해결
hour = 0
while True:
  c_list = set([])
  visited = [[False] * width for _ in range(height)]
  dfs(0, 0, c_list, visited)
  
  if len(c_list) == 0:
    break
  
  hour += 1
  prev_length = len(c_list)
  for (i, j) in list(c_list):
    square[i][j] = 0

print(hour)
print(prev_length)