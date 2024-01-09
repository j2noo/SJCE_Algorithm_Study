import sys

# 발 이동 시 비용 계산
def getCost(curr, next):
  if curr == next:
    return 1
  if curr == 0:
    return 2
  if abs(curr - next) == 2:
    return 4
  return 3

# 입력
command = list(map(int, sys.stdin.readline().split()))
command.pop()
length = len(command)

MAX = 100000 * 4

dp = [[[MAX, MAX, MAX, MAX, MAX] for _ in range(5)] for _ in range(length)]

# 1번째
dp[0][command[0]][0] = 2
dp[0][0][command[0]] = 2

# 2 ~ length번째
for i in range(1, length):
  to = command[i]
  
  # 왼발 이동 시
  for l in range(5): # 이전 왼발 상태
    for r in range(5): # 이전 오른발 상태
      dp[i][to][r] = min(dp[i-1][l][r] + getCost(l,to), dp[i][to][r])
  
  # 오른발 이동 시
  for l in range(5): # 이전 오른발 상태
    for r in range(5): # 이전 왼발 상태
      dp[i][l][to] = min(dp[i-1][l][r] + getCost(r, to), dp[i][l][to])

MIN = MAX

for i in range(5):
  for j in range(5):
    MIN = min(MIN, dp[length - 1][i][j])
    
print(MIN)