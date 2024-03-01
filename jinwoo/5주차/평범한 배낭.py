# 앞에서부터, n번째 물품에서, 남은 무게가 k일때, 가능한 최고 가치
# n번째 물품을 넣거나 안넣거나
def solve(n,k):
    if n==N:
        return 0
    
    if dp[n][k]!=-1:
        return dp[n][k]
    ans=0
    # n번쨰 넣기
    if k >= arr[n][0]:
        ans=max(ans,solve(n+1,k-arr[n][0])+arr[n][1])
    
    # n번째 안넣기
    ans=max(ans,solve(n+1,k))
    dp[n][k] = ans

    return ans

# input
N, K = map(int,input().split())
arr = []
dp = [[-1] * (K+1) for _ in range(N+1)]
for _ in range(N):
    # input 줄이기
    A, B= map(int,input().split())
    arr.append([A,B])

print(solve(0,K))