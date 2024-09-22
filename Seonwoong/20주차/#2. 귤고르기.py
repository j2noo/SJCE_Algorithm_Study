def solution(k, tangerine):
    answer = 0
    dic = {}
    
    # 귤의 종류와 개수를 세기
    for x in tangerine:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    
    # 개수가 많은 순으로 정렬
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    count = 0
    # 귤의 종류 수 세기
    for key, value in dic:  
        count += value
        answer += 1
        if count >= k:
            break
            
    return answer
