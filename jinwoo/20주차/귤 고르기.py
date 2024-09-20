def solution(k, tangerine):
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i]+=1
        else :
            dic[i] = 1
    
    # 개수별로 묶기
    cnts = []
    for key,v in dic.items():
        cnts.append(v)
    cnts.sort(reverse = True)
    
    # 앞에서부터 세어 나가기
    psum = 0
    for idx, cnt in enumerate(cnts):
        psum+=cnt
        if psum >= k:
            return idx+1
        
    answer = 0
    return answer

# 정렬? 1 2 2 3 3 4 5 5
# 1 : 1개, 2 : 2개, 3 : 2개 ... 딕셔너리 후 정렬