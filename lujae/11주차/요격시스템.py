# 시간 : 10분 51초
# 레벨 : 2

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

targets.sort(key = lambda x: x[1])

mainObj = targets[0]

answer = 1
for i in range(1, len(targets)):
    currentObj = targets[i]

    if currentObj[0] < mainObj[1]:
        continue

    mainObj = currentObj
    answer += 1

print(answer)