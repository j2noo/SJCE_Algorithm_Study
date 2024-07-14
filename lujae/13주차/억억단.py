# 시간: 1h 20m
## 소수라는 개념을 괜히 사용한듯
import math


def getPrimeList(e):
    prime = [True] * (e + 1)
    prime[1] = False
    for num in range(2, int(math.sqrt(e + 1) + 1)):
        for move in range(2 * num, e + 1, num):
            prime[move] = False

    return prime


def getEmergeCntList(e):
    isPrimeList = getPrimeList(e)
    primeNumList = [num for num in range(1, e + 1) if isPrimeList[num]]

    emergeCntList = [1] * (e + 1)


    for num in range(2, e + 1):
        if isPrimeList[num]:
            emergeCntList[num] = 2
        else:
            for divNum in primeNumList:
                if  num % divNum == 0:

                    objNum = num // divNum

                    # cnt : objNum이 가지고 있는 divNum의 인자 개수
                    cnt = 0
                    while objNum % (divNum ** (cnt + 1)) == 0:
                        cnt += 1

                    emergeCntList[num] = (emergeCntList[objNum] // (cnt + 1)) * (cnt + 2)
                    break

    for num in primeNumList:
        cnt = 1
        while num ** cnt <= e:
            emergeCntList[num ** cnt] = cnt + 1
            cnt += 1

    return emergeCntList
def solution(e, starts):
    emergeCntList = getEmergeCntList(e)
    maxEmergeNumList = [0] * (e + 1)
    answer = []

    maxCnt = 0
    maxCntNum = 0
    for i in range(e, 0, -1):
        if maxCnt <= emergeCntList[i]:
            maxCnt = emergeCntList[i]
            maxCntNum = i

        maxEmergeNumList[i] = maxCntNum


    for start in starts:
        answer.append(maxEmergeNumList[start])

    return answer