
def solution(picks, minerals):
    answer = 0
    # 미네랄 5개씩 쪼개기
    
    mineral_list=[]
    for i in range(0, len(minerals), 5):
        mineral_list.append(minerals[i:i+5])

    # 각 미네랄 묶음의 채굴 비용 계산
    costs = []
    for mineral in mineral_list:
        cost = [0, 0, 0] 
        for mine in mineral:
            if mine == 'diamond':
                cost[0], cost[1], cost[2] = cost[0]+1, cost[1]+5, cost[2]+25
            elif mine == 'iron':
                cost[0], cost[1], cost[2] = cost[0]+1, cost[1]+1, cost[2]+5
            elif mine == 'stone':
                cost[0], cost[1], cost[2] = cost[0]+1, cost[1]+1, cost[2]+1
        costs.append(cost)
    else:
        # 곡갱이 수보다 많은 광물캐는 것 불가능
        while len(costs)>sum(picks): costs.pop()
    
    # 비용이 가장 적게 드는 순서대로 정렬
    costs.sort(key=lambda x: (-x[2]))
    
    # 주어진 픽 개수 내에서 최소 비용으로 채굴
    for cost in costs:
        if picks[0] > 0:
            picks[0] -= 1
            answer += cost[0]
            continue
        if picks[1] > 0:
            picks[1] -= 1
            answer += cost[1]
            continue
        if picks[2] > 0:
            picks[2] -= 1
            answer += cost[2]
            continue
    
    return answer

# 소요시간 40분
# 시간복잡도 O(nlogn)
