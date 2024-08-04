# 6분
# lv1
# 시키는대로 구현..
def solution(s):
    ansCnt=0
    isFirst = True
    for ch in s:
        # 진입점
        if isFirst:
            target = ch
            cnt = [0,0] # target & non-target
            isFirst = False
            
        if target == ch:
            cnt[0]+=1
        else :
            cnt[1]+=1
        
        if cnt[0] == cnt[1]:
            ansCnt+=1
            isFirst = True
    
    # 끝났는데 짝이 안맞으면 1 추가
    if isFirst == False:
        ansCnt +=1
    
    return ansCnt