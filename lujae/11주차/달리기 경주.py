# 시간 : 5분 21초
# 레벨 : 1

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

rankMap = {}

for i in range(len(players)):
    rankMap[players[i]] = i

for call in callings:
    rank = rankMap[call]

    currentIdx = rank
    nextIdx = rank - 1

    players[nextIdx], players[currentIdx] = players[currentIdx], players[nextIdx]

    rankMap[players[nextIdx]] = nextIdx
    rankMap[players[currentIdx]] = currentIdx

print(players)

