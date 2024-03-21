MOVE = 'MOVE'
TURN = 'TURN'

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def turn(curr, dir):
  curr_pos, curr_dir = curr
  diff = 1 if dir == 0 else -1
  next_dir = (curr_dir + diff) % 4
  return [curr_pos, next_dir]

def move(curr, distance):
  curr_pos, curr_dir = curr
  x, y = curr_pos
  next_x = x + dx[curr_dir] * distance
  next_y = y + dy[curr_dir] * distance
  return [[next_x, next_y], curr_dir]

def process(curr, command, d):
  if command == TURN:
    curr = turn(curr, d)
  else:
    curr = move(curr, d)
  
  return curr

# M: 정사각형 S의 한 변의 길이
# n: 수행할 명령어 개수
M, n = map(int, input().split(' '))
curr = [[0, 0], EAST]
flag = True
for _ in range(n):
  command, d = input().split(' ')
  curr = process(curr, command, int(d))
  x, y = curr[0]
  if not(0 <= x <= M and 0 <= y <= M):
    flag = False

if (flag):
  x, y = curr[0]
  print(x, y)
else:
  print(-1)