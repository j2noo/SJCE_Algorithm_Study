def solution(s):
    answer = [-1] * len(s)
    
    for i in range(len(s)):
        for j in range(i):
            if s[i]==s[j]: answer[i]=i-j
                
    return answer
