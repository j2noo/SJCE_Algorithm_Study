def solution(t, p):
    answer,n,size=0,len(t),len(p)
    
    for i in range(n-size+1): 
        if int(p)>=int(t[i:i+size]): answer+=1
        
    return answer
