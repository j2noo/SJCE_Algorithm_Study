import itertools
def solution(orders, course):
    def backTrack(od1,od2,r,c,dp):
        # 같은메뉴
        if r==-1 or c==-1:
            return ""
        if od1[r]==od2[c]:
            return backTrack(od1,od2,r-1,c-1,dp) + od1[r] 
        elif dp[r-1][c] >= dp[r][c-1]:
            return backTrack(od1,od2,r-1,c,dp)
        else :
            return backTrack(od1,od2,r,c-1,dp) 
        
    def LCS(od1, od2):
        # dp[n][m] : n번째와 m번쨰 인덱스가지 가장 많이 겹치는 횟수
        dp = [[0]*12 for _ in range(12)]
        sze1 = len(od1)
        sze2 = len(od2)
        print(od1,od2)
        for i in range(sze1):
            for j in range(sze2):
                if od1[i] ==od2[j]:
                    # idx가 -1인경우 처리 안해도 됨 ㅋㅋ
                    dp[i][j] = dp[i-1][j-1]+1
                else :
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # 역추적
        # for i in range(sze1):
            # print(dp[i])
        res = backTrack(od1,od2,sze1-1,sze2-1,dp)
        print("res",res)
        return res
                    
        
    sorted_li = []
    sze = len(orders)
    # order 내부 정렬
    for order in orders :
        str_li = []
        for st in order:
            str_li.append(st)
        str_li.sort()
        sorted_li.append(str_li)
        
    answer = {}
    # 자신보다 큰 idx와 LCS
    for i in range(sze):
        for j in range(i+1, sze):
            print(i,j)
            ret = LCS(sorted_li[i],sorted_li[j])
            if len(ret)<2 :
                continue
            print("amns :",ret)
            for k in range(2,len(ret)+1):
                combs = list(itertools.combinations(ret,k))
                for comb in combs:
                    strs = ""
                    for str in comb:
                        strs+=str                        
                    print("comb:",strs)
                    if strs in answer:
                        answer[strs]+=1
                    else :
                        answer[strs]=1
    
    print(answer)
    return answer

# orders : 20, 각각의 길이 : 10
# 26C10? X

# LCS 알고리즘 -> 두 손님끼리 제일 많이 겹치는 것 찾기 가능
# 3,4 -> CDE -> CD,CD,DE,CDE
# 3,5 -> DE  -> DE
# 자신보다 큰 번호의 손님과 LCS