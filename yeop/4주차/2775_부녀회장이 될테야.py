# a층의 b호에 살려면 (a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다.
# 0층부터, 1호부터

# 입력
T = int(input())
for _ in range(T):
  k = int(input()) # 층
  n = int(input()) # 호
  dp = [[0] * n for i in range(k + 1)]
  
  # 0층
  for i in range(n):
    dp[0][i] = i + 1
    
  # 1 ~ k층
  for level in range(1, k + 1):
    for i in range(n):
      dp[level][i] = sum(dp[level - 1][0:i+1])
  
  print(dp[k][n - 1])
  