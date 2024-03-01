N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range (1, N):
    for j in range (i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 유용했던 반례
# 11
# 100 1 2 3 101 4 5 6 102 7 8
# 정답 - 8

# 20
# 322 831 212 232 545 698 260 265 324 215 701 75 156 605 851 993 425 887 691 593
# 정답 - 8