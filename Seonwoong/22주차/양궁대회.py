from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_score = 0
    max_combination = {}
    answer = [0] * 11
    
    for c in combinations_with_replacement(range(11), n):
        ryan = Counter(c)
        apeach_score, ryan_score = 0, 0
        
        for i in range(11):
            if info[10 - i] < ryan[i]:
                ryan_score += i
            elif info[10 - i] > 0:
                apeach_score += i
                
        if ryan_score - apeach_score > max_score:
            max_score = ryan_score - apeach_score
            max_combination = ryan
            
    if max_score == 0:
        return [-1]
    
    for i in range(11):
        answer[10 - i] = max_combination[i]
        
    return answer

# 파이썬 라이브러리 활용? 가장 낮은 점수를 더 많이 맞힌 경우를 return이 되는지
# 같은 점수 차가 여러개 있을 경우 가장 첫 번째 조합만 들어가게 되는데
# 이 때 조합은 뒤에서부터 숫자가 바뀌기 때문에 가장 낮은 점수를 가장 많이 맞힌 조합이 들어가게 되고 순서를 신경 쓰지 않아도 됨
# 시간복잡도가 매우 높아 다른 방법으로 하는 것이 맞을지도
