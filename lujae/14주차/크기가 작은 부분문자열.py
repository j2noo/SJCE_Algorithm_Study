#시간 : 6분 50초

def convertToNumber(strNum):
    return int(strNum)


def solution(t, p):
    answer = 0

    tLen = len(t)
    pLen = len(p)

    for i in range(tLen - pLen + 1):
        if convertToNumber(t[i:i + pLen]) <= convertToNumber(p):
            answer += 1

    return answer