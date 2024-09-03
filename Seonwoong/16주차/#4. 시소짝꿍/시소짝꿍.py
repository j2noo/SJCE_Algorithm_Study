from collections import Counter

def solution(weights):
    answer=0
    weights=Counter(weights)
    
    for i in weights:
        answer+=weights[i]*(weights[i]-1)/2
        answer+=weights[i]*weights[i*(2/1)]
        answer+=weights[i]*weights[i*(3/2)]
        answer+=weights[i]*weights[i*(4/3)]
    
    return answer
