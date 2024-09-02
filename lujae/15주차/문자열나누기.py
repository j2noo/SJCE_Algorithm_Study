# 시간: 8분
## 구현 문제

def solution(s):
    answer = 0

    cntX = cntNotX = 0

    for i in range(len(s)):
        if cntX == 0:
            x = s[i]
            cntX = 1
        elif s[i] == x:
            cntX += 1
        else:
            cntNotX += 1

        if cntX == cntNotX:
            print("x = %s, endIdx = %d" %(x, i))
            answer += 1
            cntX = cntNotX = 0

    if cntX != cntNotX:
        answer += 1

    return answer

solution("abracadabra")