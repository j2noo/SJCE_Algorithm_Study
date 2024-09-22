# 시간: 10분
# 수학

import math
def solution(k, d):
    answer = 0

    for x in range(0, d + 1, k):
        if x > d: break

        max_y = int(math.sqrt(d ** 2 - x ** 2))
        answer += max_y // k + 1

    return answer