def sol(n, seq):
  dp = [0 for i in range(n)]
  
  for i in range(n):
    maxLength = 0
    
    for j in range(0, i):
      if (dp[j] > maxLength and seq[j] < seq[i]):
        maxLength = dp[j]
    
    dp[i] = maxLength + 1
  
  return max(dp)

n = int(input())
seq = list(map(int, input().split()))

print(sol(n ,seq))
