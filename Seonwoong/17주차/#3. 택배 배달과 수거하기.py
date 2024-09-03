def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0
    pickup = 0

    for i in range(n-1, -1, -1):
        #현재 위치의 택배가 배달해야 할 택배나 수거해야 할 택배가 있는지 확인
        if deliveries[i] != 0 or pickups[i] != 0:

            #delivery 변수와 pickup 변수가 해당 위치의 택배 개수보다 작을 때까지
            while delivery < deliveries[i] or pickup < pickups[i]:
                delivery += cap
                pickup += cap
                answer += (i + 1) * 2

            # 배달한 택배와 수거한 택배의 개수를 각각 차감
            delivery -= deliveries[i]
            pickup -= pickups[i] 

    return answer
