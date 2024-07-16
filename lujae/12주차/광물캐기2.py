##
##
## 문제 잘 못 이해함 => 다이아 곡괭이를 사용하면, 사지고 있는 다이아 곡괭이를 전부 사용하는줄
def calCost(canRange, minerals, pickIdx, startIdx):
    ret = 0

    costMap = []
    costMap.append({"diamond":1, "iron":1, "stone":1})
    costMap.append({"diamond":5, "iron":1, "stone":1})
    costMap.append({"diamond":25, "iron":5, "stone":1})


    for i in range(startIdx, startIdx + canRange[pickIdx]):
        if i >= len(minerals):
            break
        ret += costMap[pickIdx][minerals[i]]

    return ret
def solution(picks, minerals):
    answer = 0

    canRange = [picks[i] * 5 for i in range(3)]

    if canRange[0] >= len(minerals):
        answer = len(minerals)
    elif canRange[0] + canRange[1] >= len(minerals):
        diaFirstCost = calCost(canRange, minerals, 0, 0) + calCost(canRange, minerals, 1, canRange[0])
        ironFirstCost = calCost(canRange, minerals, 1, 0) + calCost(canRange, minerals, 0, canRange[1])
        answer = min(diaFirstCost, ironFirstCost)
    else:
        diaFirstCost = calCost(canRange, minerals, 0, 0) + min(
            calCost(canRange, minerals, 1, canRange[0]) + calCost(canRange, minerals, 2, canRange[0] + canRange[1]),
            calCost(canRange, minerals, 2, canRange[0]) + calCost(canRange, minerals, 1, canRange[0] + canRange[2])
        )

        ironFirstCost = calCost(canRange, minerals, 1, 0) + min(
            calCost(canRange, minerals, 0, canRange[1]) + calCost(canRange, minerals, 2, canRange[1] + canRange[0]),
            calCost(canRange, minerals, 2, canRange[1]) + calCost(canRange, minerals, 0, canRange[1] + canRange[2])
        )

        stoneFirstCost = calCost(canRange, minerals, 2, 0) + min(
            calCost(canRange, minerals, 0, canRange[2]) + calCost(canRange, minerals, 1, canRange[2] + canRange[0]),
            calCost(canRange, minerals, 1, canRange[2]) + calCost(canRange, minerals, 0, canRange[2] + canRange[1])
        )

        answer = min(diaFirstCost, ironFirstCost, stoneFirstCost)

    return answer

picks = [1, 0, 2]
minerals = ["iron", "iron", "iron", "iron", "iron", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]

print(solution(picks, minerals))