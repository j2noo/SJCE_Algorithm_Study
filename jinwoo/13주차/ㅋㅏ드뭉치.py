#시간 : 15분
# 레벨 : 1
from collections import deque

def solution(cards1, cards2, goal):
    stack1, stack2 = deque(), deque()
    for card1 in cards1:
        stack1.append(card1)
    for card2 in cards2:
        stack2.append(card2)
        
    for word in goal:
        
        if stack1 and stack1[0] == word:
            stack1.popleft()
        elif stack2 and stack2[0] == word:
            stack2.popleft()
        else :
            return "No"
    
    return "Yes"
    answer = ''
    return answer

#. 1 10개, 2 10개를 나열하는것.
# 20C10 -> 18만

# solve2. goal에서 찾은게 cards에 있는지 확인
