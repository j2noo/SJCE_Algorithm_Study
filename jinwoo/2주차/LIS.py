print(0.9%0.2)

N=int(input())

arr = list(map(int,input().split()))

dp = [1]*N
ans=1

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i]    =   max(dp[i],dp[j]+1)
            ans=max(ans,dp[i])
print(ans)