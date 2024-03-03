import sys

input = sys.stdin.readline

def sol(dp, items, N, K):
  for i in range(1, N + 1): # i번째 아이템 
    for w in range(1, K + 1): # 배낭 무게 제한 w
      weight, value = items[i - 1]
      if (weight > w):
        dp[i][w] = dp[i-1][w]
      else:
        dp[i][w] = max(value + dp[i-1][w-weight], dp[i-1][w])
  
  return dp[N][K]

# N: 물품의 수 - dp의 행
# K: 준서가 버틸 수 있는 무게 - dp의 열
# W: 물건의 무게
# V: 물건의 가치

# 입력
N, K = map(int, input().split())
items = []
for _ in range(N):
  W, V = map(int, input().split())
  items.append([W, V])
  
dp = [[0] * (K + 1) for _ in range(N + 1)]

print(sol(dp, items, N, K))