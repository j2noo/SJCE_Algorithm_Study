# 시간 : 4분 48초
# 레벨 : 1

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

answer = []
scoreMap = {}
for i in range(len(yearning)):
    scoreMap[name[i]] = yearning[i]

for names in photo:
    totalScore = 0
    for peopleName in names:
        if peopleName in scoreMap:
            totalScore += scoreMap[peopleName]
    answer.append(totalScore)

print(answer)