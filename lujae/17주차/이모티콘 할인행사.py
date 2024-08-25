## 시간 30분
def getRatesList(n, pos, ret, tmp):
    rates = [10, 20, 30, 40]

    if pos == n:
        ret.append(tmp)
        return

    for i in range(4):
        getRatesList(n, pos + 1, ret, tmp + [rates[i]])

def solution(users, emoticons):
    answer = [0, 0]

    ratesList = []
    getRatesList(len(emoticons), 0, ratesList, [])

    for rates in ratesList:
        caseRet = [0, 0]

        for user in users:
            userPriceSum = 0

            for i in range(len(emoticons)):
                if user[0] <= rates[i]:
                    userPriceSum += emoticons[i] * (100 - rates[i]) / 100

            if userPriceSum >= user[1]:
                caseRet[0] += 1
            else:
                caseRet[1] += userPriceSum

        if caseRet[0] > answer[0]:
            answer[0] = caseRet[0]
            answer[1] = caseRet[1]
        elif caseRet[0] == answer[0] and caseRet[1] > answer[1]:
            answer[0] = caseRet[0]
            answer[1] = caseRet[1]

    answer[1] = int(answer[1])
    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))