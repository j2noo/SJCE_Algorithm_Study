import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = []
for _ in range(R):
  row = list(input().rstrip())
  board.append(row)

def is_valid(i, j):
  return 0 <= i < R and 0 <= j < C

def dfs(row, col):
  board[row][col] = 'x'
  
  if col == C - 1:
    return True
  
  next_node = []
  for dy in range(-1, 2):
    next_row, next_col = [row+dy, col+1]
    if is_valid(next_row, next_col) and board[next_row][next_col] != 'x':
      next_node.append([next_row, next_col])
    
  for next_row, next_col in next_node:
    flag = dfs(next_row, next_col)
    if flag:
      return True
  
# 최대한 밀착해서 가자.
count = 0
for i in range(R):
  flag = dfs(i, 0)
  if flag:
    count += 1
    
print(count)