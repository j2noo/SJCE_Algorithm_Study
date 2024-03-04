a = input()
b = input()
dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

# 배낭문제와 유사
# 세로 줄에는 a 문자열을 가로 줄에는 b 문자열을 놓고 비교
# 직접 표 그리면서 이해해보기
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(map(max, dp)))