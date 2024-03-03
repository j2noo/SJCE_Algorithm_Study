N = int(input())

dp = [[0 for j in range(10)] for i in range(100)]
# dp[len-1][num] = 시작 숫자가 num이고 길이가 len인 계단수의 개수
# ex) 시작 숫자가 1이고 길이가 3이면 -> dp[0][2]

# 길이 1, 2 초기화
dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp[1] = [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]

# ~100까지
for len in range(2, 100):
  for num in range(10):
    if (num == 0):
      dp[len][0] = dp[len - 1][1]
    elif (num == 9):
      dp[len][9] = dp[len - 1][8]
    else:
      dp[len][num] = dp[len - 1][num - 1] + dp[len - 1][num + 1]
  
total = 0
for i in range(1, 10):
  total += dp[N - 1][i]
  
print(total % 1000000000)


