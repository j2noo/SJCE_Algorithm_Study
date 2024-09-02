def solution(s, skip, index):
    answer = []

    sequence = []
    for ch in range(ord('a'), ord('z') + 1):
        sequence.append(chr(ch))
    nextAlpha = []

    for i in range(len(sequence)):
        cnt = 0
        alphaIdx = i

        if i == 1:
            print("12")
        while cnt < index:
            alphaIdx += 1
            alphaIdx %= len(sequence)

            if sequence[alphaIdx] not in skip:
                cnt += 1

        nextAlpha.append(sequence[alphaIdx])

    for ch in s:
        answer.append(nextAlpha[ord(ch) - ord('a')])

    return "".join(answer)

solution("aukks", "wbqd", 5)