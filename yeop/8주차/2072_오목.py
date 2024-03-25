# 19 x 19, (1, 1) ~ (19, 19)
EMPTY = 0
BLACK = 1
WHITE = 2

COLUMN = 0
ROW = 1
DIAGONAL1 = 2
DIAGONAL2 = 3

# 오목 탐색
# 육목은 인정 안함.

# 입력
N = int(input())
event = [[-1, -1]]
board = [[EMPTY] * 20 for _ in range(20)]

for i in range(N):
  row, col = map(int, input().split(' '))
  event.append([row, col])

# 특정 방향으로 연속된 숫자의 개수를 구하는 함수
def check_seq_num(row, col, color, visited, direction):
  # 인덱스 조건 만족, 같은 컬러일 경우
  if (1 <= row < 20 and 1 <= col < 20) and board[row][col] == color and visited[row][col] == False:
    visited[row][col] = True
    
    # 위아래
    if (direction == COLUMN):
      next1 = [row - 1, col]
      next2 = [row + 1, col]
      
    # 양옆
    elif (direction == ROW):
      next1 = [row, col - 1]
      next2 = [row, col + 1]
    
    # 대각선1
    elif (direction == DIAGONAL1):
      next1 = [row - 1, col - 1]
      next2 = [row + 1, col + 1]
    
    # 대각선2
    else:
      next1 = [row - 1, col + 1]
      next2 = [row + 1, col - 1]
    
    return 1 + check_seq_num(next1[0], next1[1], color, visited, direction) + check_seq_num(next2[0], next2[1], color, visited, direction)
  
  # 연속되지 않을 경우
  return 0

# 오목 확인 함수
def solve(row, col, color):
  for direction in range(4):
    visited = [[False] * 20 for _ in range(20)] # 탐색했는지 알아보는 체크용 2차원 배열
    num = check_seq_num(row, col, color, visited, direction) # 연속되는 숫자의 수
    if (num == 5):
      return True
  
  return False

# 해결
answer = -1
for i in range(1, N + 1):
  row, col = event[i]  
  board[row][col] = BLACK if i % 2 == 1 else WHITE
  color = BLACK if i % 2 == 1 else WHITE
  result = solve(row, col, color)
  if (result):
    answer = i
    break

print(answer)