import sys
sys.setrecursionlimit(10**5)
#idx1, idx2 글자부터 시작했을 때 LCS의 길이
def solve(idx1, idx2):
    if (idx1 == len(str1)) or (idx2 == len(str2)):
        return 0
    
    if dp[idx1][idx2]!= -1:
        return dp[idx1][idx2]
    
    if str1[idx1] == str2[idx2]:
        dp[idx1][idx2] = solve(idx1+1,idx2+1)+1
        return dp[idx1][idx2]
    
    dp[idx1][idx2]  = max(solve(idx1+1,idx2),solve(idx1,idx2+1))
    return  dp[idx1][idx2]  

str1 = input()
str2 = input()


# i,j번 글자부터 시작했을때 LCS의 길이.
dp = [[-1]*1001 for _ in range(1001)]

print(solve(0,0))