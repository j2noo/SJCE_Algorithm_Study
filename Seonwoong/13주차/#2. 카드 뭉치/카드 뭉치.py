from collections import deque

def solution(cards1, cards2, goal):
    answer="Yes"
    #deque로 card1, card2 자료구조 변경 -> 시간복잡도 낮은 popleft쓰기 위해
    cards1=deque(cards1)
    cards2=deque(cards2)
    
    #goal의 첫 원소부터 cards1[0]와 cards2[0]가 있는지 확인
    #있다면 해당 cards의 첫 원소 popleft()
    #없다면 answer=NO, break 
    for i in range(len(goal)):
        if cards1 and cards1[0]==goal[i]:
            cards1.popleft()
        elif cards2 and cards2[0]==goal[i]:
            cards2.popleft()
        else:
            answer="No"
            break
    
    return answer

#시간 10분
#시간복잡도 O(N)
