dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
board = []
for _ in range(N):
  row = list(map(int, input().split()))
  board.append(row)

def is_valid(i, j):
  return 0 <= i < N and 0 <= j < M

def dfs(i, j, depth, prev):
  if depth > 3 or (not is_valid(i, j)):
    return 0
  
  result = [0, 0, 0, 0]
  for k in range(4):
    x = j + dx[k]
    y = i + dy[k]
    if y == prev[0] and x == prev[1]:
      continue
    result[k] = dfs(y, x, depth + 1, [i, j])
  
  return board[i][j] + max(result)

def ewsn(i, j):
  result = [0, 0, 0, 0]
  for k in range(4):
    x = j + dx[k]
    y = i + dy[k]
    if not is_valid(y, x):
      continue
    result[k] = board[y][x]
  return board[i][j] + sum(result) - min(result)
    

max_board = [[0] * M for _ in range(N)]
for i in range(N):
  for j in range(M):
    max_board[i][j] = max(dfs(i, j, 0, [i, j]), ewsn(i, j))

answer = 0
for i in range(N):
  # print(max_board[i])
  answer = max(answer, max(max_board[i]))

print(answer)