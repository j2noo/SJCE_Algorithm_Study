# 시간 50분
# 그리디로 가장 먼 곳 부터 해결을 해야함
# 택배를 배달해야하는 곳을 먼곳부터

import heapq


def solution(cap, n, deliveries, pickups):
    answer = 0

    newDeliveries = []
    newPickups = []

    lists = [newDeliveries, newPickups]
    for i in range(n):
        cost = i + 1

        if deliveries[i] != 0:
            heapq.heappush(newDeliveries, (-cost, deliveries[i]))
        if pickups[i] != 0:
            heapq.heappush(newPickups, (-cost, pickups[i]))

    while not (len(newDeliveries) == 0 and len(newPickups) == 0):
        dCost = 0
        if len(newDeliveries) > 0:
            dCost = -newDeliveries[0][0]

        pCost = 0
        if len(newPickups) > 0:
            pCost = -newPickups[0][0]

        answer += 2 * max(dCost, pCost)
        print(answer)

        for li in lists:
            minusValue = cap
            while minusValue > 0 and len(li) > 0:
                pop = heapq.heappop(li)

                cost = -pop[0]
                cnt = pop[1]

                if minusValue - cnt >= 0:
                    minusValue -= cnt
                    cnt = 0
                else:
                    cnt = cnt - minusValue
                    minusValue = 0

                if cnt > 0:
                    heapq.heappush(li, (-cost, cnt))

    return answer

print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))