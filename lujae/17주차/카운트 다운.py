def solution(target):
    cntDart = 0
    cntSingle = 0
    cntBull = 0

    canScore = [False for i in range(61)]
    doubleSingleCanScore = [False for i in range(41)]
    canScore[50] = True

    for i in range(1, 21):
        canScore[i] = True
        canScore[2 * i] = True
        canScore[3 * i] = True

    for i in range(1, 21):
        for j in range(1, 21):
            doubleSingleCanScore[i + j] = True

    cnt60 = target // 60
    cnt50 = target // 50
    
    cntDart += cnt60
    target -= 60 * cnt60

    # for i in range(1, 41):
    #     if not canScore[i] and not doubleSingleCanScore[i]:
    #         print(i)

    if target == 50:
        cntDart += 1
        cntBull += 1
    elif target > 0:
        if canScore[target]:
            cntDart += 1
            if 1 <= target <= 20:
                cntSingle += 1
        else:
            if target > 50:
                cntDart += 2
                cntBull += 1
                cntSingle += 1
            elif doubleSingleCanScore[target]:
                cntDart += 2
                cntSingle += 2
            else:
                cntDart += 2
                cntSingle += 1

    return [cntDart, cntSingle + cntBull]

print(solution(241))