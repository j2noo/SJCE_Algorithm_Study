n = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

# dp배열은 i번째까지 최소로 필요한 편집 횟수
dp = [0] * (n+1)
# 인덴트 차이
diff = [0] * (n+1)

# 인덴트 차이를 저장
for i in range(0, n):
    diff[i] = arrA[i] - arrB[i]

# 일단 첫 차이만큼 편집해야함
dp[0] = abs(diff[0])

for i in range(1, n):
    # 부호가 같다면
    if diff[i]*diff[i-1] > 0:
        # 전보다 더 많이 인덴트 해야된다면 그 차이만큼 추가
        if abs(diff[i]) > abs(diff[i-1]):
            dp[i] = dp[i-1] + (abs(diff[i]) - abs(diff[i-1]))
        # 아니라면 한줄로 편집가능
        else:
            dp[i] = dp[i-1]
    # 부호가 다르면 다시 첫 차이만큼 편집
    else:
        dp[i] = dp[i-1] + abs(diff[i])
print(dp[n-1])
