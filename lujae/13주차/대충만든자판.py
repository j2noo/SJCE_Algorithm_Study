#시간: 9분 50초
def solution(keymap, targets):
    INF = 9877654321
    answer = []

    cntDic = {}

    for ch in range(ord('A'), ord('Z') + 1):
        cntDic[chr(ch)] = INF

    for key in keymap:
        for i in range(len(key)):
            cntDic[key[i]] = min(cntDic[key[i]], i + 1)

    for target in targets:
        ret = 0
        for ch in target:
            if cntDic[ch] == INF:
                ret = -1
                break
            else:
                ret += cntDic[ch]

        answer.append(ret)

    return answer

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
print(solution(
    keymap, targets
))