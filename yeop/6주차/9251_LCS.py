str1 = input()
str2 = input()
str1_len = len(str1)
str2_len = len(str2)

# dp[i][j] = str1의 i번째, str2의 j번째에서 시작해서 가장 긴 부분 수열 수
dp = [[0] * str2_len for _ in range(str1_len)]

# 마지막 행 / 열 초기화
for i in range(str2_len):
  find_char = str1[-1]
  idx = str2.find(find_char, i)
  
  if (idx == -1):
    dp[-1][i] = 0
  else:
    dp[-1][i] = 1
    
for i in range(str1_len):
  find_char = str2[-1]
  idx = str1.find(find_char, i)
  
  if (idx == -1):
    dp[i][-1] = 0
  else:
    dp[i][-1] = 1

# 메인 로직
for i in range(str1_len - 2, -1, -1):
  for j in range(str2_len - 2, -1, -1):
    if str1[i] == str2[j]:
      dp[i][j] = 1 + dp[i+1][j+1]
    else:
      dp[i][j] = max(dp[i+1][j], dp[i][j+1])
  
# 답
answer = 0    
for i in range(str1_len):
  answer = max(max(dp[i]), answer)
  
print(answer)