import sys

input = sys.stdin.readline


# 입력
n, m = list(map(int, input().split()))
matrix = []
for _ in range(n):
  row = list(map(int, list(input().strip())))
  matrix.append(row)
  
dp = [[0] * m for _ in range(n)]

# 1열 초기화
for i in range(n):
  dp[i][0] = matrix[i][0]

# 1행 초기화
for j in range(m):
  dp[0][j] = matrix[0][j]

# (1, 1) 부터 시작
for i in range(1, n):
  for j in range(1, m):
    if matrix[i][j] > 0:
      dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

# 전체 순회하면서 최대값 찾기
length = max(max(row) for row in dp)
print(length ** 2)