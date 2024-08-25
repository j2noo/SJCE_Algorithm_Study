# 시간: 30분
# 수학 개 어렵네

import math

def calCntPointWithLine(r):
    ret = 4 * r + 1

    for x in range(1, r):
        yMax = int(math.sqrt(r ** 2 - x ** 2))
        ret += 4 * yMax

    return ret


def calCntPointWithoutLine(r):
    ret = 4 * r + 1

    for x in range(1, r):
        yMax = int(math.sqrt(r ** 2 - x ** 2))

        if yMax ** 2 + x ** 2 == r ** 2:
            yMax -= 1

        ret += 4 * yMax

    return ret - 4


def solution(r1, r2):
    cntR1 = calCntPointWithoutLine(r1)
    cntR2 = calCntPointWithLine(r2)

    answer = cntR2 - cntR1
    return answer