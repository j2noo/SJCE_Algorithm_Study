# 12qns
def solution(triangle):
    dp = [[-1] * 501 for _ in range(501)]
    dp[0][0] = triangle[0][0]
    for i,li in enumerate(triangle):
        if i==0 :
            continue
        for j in range(len(li)):
            if j==0 :
                dp[i][j] = dp[i-1][j]+triangle[i][j]
            else :
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        
    answer = max(dp[len(triangle)-1])
    return answer

# dp[500][500]