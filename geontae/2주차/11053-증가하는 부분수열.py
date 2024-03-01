n = int(input())
arr = list(map(int, input().split()))

dp = [1]*n

for i in range(0, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            # 처음부터 올라오면서 가장 긴 부분수열을 dp에 등록
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 거꾸로 해서도 생각해보기
