def solution(targets):
    
    target=sorted(targets, key=lambda x: x[1])
    
    #print(target)
    answer, end= 0,0
    for s, e in target:
        if s>=end:
            answer+=1
            end=e
    return answer
                  
