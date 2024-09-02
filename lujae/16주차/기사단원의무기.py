# 시간 19분
# number와 n을 헷갈림

import math
def solution(number, limit, power):
    answer = 1

    for n in range(2, number + 1):
        pCnt = 0

        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0: pCnt += 1

        pCnt *= 2

        if int (math.sqrt(n)) * int (math.sqrt(n)) == n:
            pCnt -= 1
        print(pCnt)

        if pCnt > limit:
            pCnt = power

        answer += pCnt


    return answer

solution(5, 3, 2)