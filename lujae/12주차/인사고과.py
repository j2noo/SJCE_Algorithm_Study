## 시간: 50분 // 시간 줄이는게 시간 오래걸림 (휴리스틱)

def checkNoInsentive(scores):
    for i in range(1, len(scores)):
        if scores[0][0] < scores[i][0] and scores[0][1] < scores[i][1]:
            return True

    return False
def calculateExcludedIndex(sortedScores):
    ret = [False] * len(sortedScores)

    idx = 0
    while idx < len(sortedScores):
        x, y = sortedScores[idx]

        for i in range(idx + 1, len(sortedScores)):
            if not ret[idx] and sortedScores[i][0] < x and sortedScores[i][1] < y:
                ret[i] = True

        # 다음 기준점을 계산하는 반복문
        # 이미 제외된 기준점 or 기준점의 x 좌표가 현재의 기준점과 동일하거나 or y 좌표가 현재의 기준점보다 작거나
        idx += 1
        while idx < len(sortedScores) and (ret[idx] or x == sortedScores[idx][0] or y >= sortedScores[idx][1]):
            idx += 1

    return ret

def solution(scores):
    answer = 1

    if len(scores) == 1:
        return 1

    if checkNoInsentive(scores):
        return -1

    wanhoScore = scores[0][0]  + scores[0][1]
    scores.sort(key = lambda x : (-x[0], -x[1]))

    sumList = list(map(lambda x : x[0] + x[1], scores))
    excludedIndex = calculateExcludedIndex(scores)

    for i in range(0, len(scores)):
        if not excludedIndex[i] and wanhoScore < sumList[i]:
            answer += 1

    return answer