import sys

input = sys.stdin.readline

# state
# 0: 가로
# 1: 세로
# 2: 대각선
def sol(home, N): # dp[row][col][state]
  dp = [[[0 for _ in range(3)] for _ in range(N) ] for _ in range(N)]
  # 0행 세팅
  dp[0][1][0] = 1
  for c in range(2, N):
    if home[0][c] == 0:
      dp[0][c][0] = dp[0][c - 1][0]
  
  # 1행부터 게임 시작
  for r in range(1, N):
    for c in range(1, N):
      if (home[r][c] == 0):
        # 가로 가능?
        dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]
        # 세로 가능?
        dp[r][c][1] = dp[r - 1][c][1] + dp[r - 1][c][2]
        # 대각선 가능?
        if (home[r][c - 1] == 0 and home[r - 1][c] == 0):
          dp[r][c][2] = dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]
          
  ret = dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2]
  
  return ret
      
  
# 입력
N = int(input()) # 집의 크기 N
home = []
for i in range(N):
    row = list(map(int, input().split()))
    home.append(row)
    
print(sol(home, N))