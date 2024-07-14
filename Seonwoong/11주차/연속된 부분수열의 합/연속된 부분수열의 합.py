def solution(sequence, k):
    s,e=0,0
    n=len(sequence)
    answer=[]
    
    for i in range(n):
        while s<k and e<n:
            s+=sequence[e]
            e+=1
        if s==k:
            answer.append([i,e-1])
        s-=sequence[i]
        
    answer.sort(key=lambda x: x[1]-x[0])
    
    return answer[0]
