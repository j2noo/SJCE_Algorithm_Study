def solution(info, query):
    # score와 같거나큰 첫 번째 인덱스 반환하는 이분탐색
    def findIdx(score):
        sze = len(score_li)
        lo, hi = 0, sze
        
        while(lo + 1 < hi):
            mid = (lo+hi)//2
            if score_li[mid] >= score:
                hi = mid
            else :
                lo = mid
        # print(lo, score_li[lo])
        if score_li[lo] < score:
            lo+=1
        return lo
                
    info_li = []
    query_li =[]
    score_li = []
    
    for inf in info:
        info_li.append(list(inf.split()))
        
    info_li.sort(key = lambda x : int(x[4]))
    
    for info_item in info_li:
        score_li.append(int(info_item[4]))
    
#     print(score_li)
#     for e in info_li:
#         print(e)
    
    for qur in query:
        query_li.append(list(qur.split()))
    
    answer = []
    for qr in query_li:
        language = qr[0]
        fb = qr[2]
        js = qr[4]
        food = qr[6]
        score = int(qr[7])
        idx = findIdx(score)
        # print('idx : ',idx)
        count=0
        for i in range(idx,len(info_li)):
            info_item = info_li[i]
            if (language == "-" or language == info_item[0]) and (fb == "-" or fb == info_item[1]) and (js == "-" or js == info_item[2]) and (food == "-" or food == info_item[3]):
                # print('i : ',i)
                count+=1
        # print("@@")
        answer.append(count)
        
    return answer

# 코테점수로 정렬
# 이분탐색 -> 해당점수 인덱스부터만 완탐