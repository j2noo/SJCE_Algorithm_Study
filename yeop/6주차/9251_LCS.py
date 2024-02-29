# 입력
str1 = input()
str2 = input()
str1_len = len(str1)
str2_len = len(str2)

# dp배열 초기화
# dp[i][j] = str1의 i번째, str2의 j번째에서 시작해서 가장 긴 부분 수열 수
dp = [[0] * str2_len for _ in range(str1_len)]

# 마지막 행 초기화
for i in range(str2_len):
  find_char = str1[str1_len - 1]
  idx = str2.find(find_char, i)
  
  dp[str1_len - 1][i] = idx != -1

# 마지막 열 초기화
for i in range(str1_len):
  find_char = str2[str2_len - 1]
  idx = str1.find(find_char, i)
  
  dp[i][str2_len - 1] = idx != -1

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