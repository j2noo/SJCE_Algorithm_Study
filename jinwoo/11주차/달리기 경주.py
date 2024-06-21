# 20분?
# Lv 1
def solution(players, callings):
    # 순위를 저장하는 딕셔너리
    dic={}
    for i in range(len(players)):
        dic[players[i]] = i
        

    
    # callings
    for player in callings:
        # 불린 사람의 현재 순위
        rank = dic[player]
        # 앞 사람
        frontPlayer = players[rank-1]
        
        # 스왑
        players[rank], players[rank-1] = players[rank-1], players[rank]
        # 순위 변경
        dic[player], dic[frontPlayer] =  dic[frontPlayer], dic[player]

    return players


# callings의 사람이 현재 몇 등인지 파악해야 함
# callings를 등수(idx) 배열로 만들기
# players에서 kai를 O(n)이 아닌 시간에 찾는게 관건 -> 딕셔너리