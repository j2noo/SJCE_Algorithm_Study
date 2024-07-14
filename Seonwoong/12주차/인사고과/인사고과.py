# 해결하지 못한 문제..
# 13주차에 도전
# 240713 풀이

def solution(scores):
    rank=1
    
    if len(scores)==1:
        return 1
    
    wanho=scores[0]
    wanho_score=sum(wanho)
    # 근무태도를 내림차순으로 정렬, 같은 근무태도점수 기준으로는 동료평가 점수를 오름차순을 정렬
    scores.sort(key=lambda x:(-x[0],x[1]))
    tmp=0
    
    for score in scores:
        if wanho[0]<score[0] and wanho[1]<score[1]:
            return -1
        
        # 완호 점수보다 작고, 동료점수의 최댓값보다 작은 사람은 받지 못함
        if wanho_score<sum(score) and tmp<=score[1]:
            rank+=1
            tmp=score[1]
    
    return rank

