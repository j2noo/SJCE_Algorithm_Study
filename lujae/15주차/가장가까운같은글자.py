# 시간: 4분
## 구현 문제

def solution(s):
    answer = []

    idxDic = dict()

    for i in range(ord('a'), ord('z') + 1):
        idxDic[chr(i)] = -1

    for i in range(len(s)):
        beforeIdx = idxDic[s[i]]

        if beforeIdx == -1:
            answer.append(-1)
        else:
            answer.append(i - beforeIdx)

        idxDic[s[i]] = i

    return answer
