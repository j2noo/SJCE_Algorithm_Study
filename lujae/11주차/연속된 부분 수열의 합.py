# 시간 : 19분 10초
# 레벨 : 2

sequence = 	[1, 2, 3, 4, 5]
k = 7

s = 0
e = 0

answer = []
tmpSum = sequence[0]
while s < len(sequence) and e < len(sequence):
    if tmpSum < k:
        if e < len(sequence) - 1:
            e += 1
            tmpSum += sequence[e]
        else:
            break
    elif tmpSum > k:
        if s < len(sequence) - 1:
            tmpSum -= sequence[s]
            s += 1
        else:
            break
    else:
        tmpList = [s, e]
        answer.append(tmpList)
        tmpSum -= sequence[s]
        s += 1


answer.sort(key=lambda x: (x[1] - x[0], x[0]))

print(answer[0])
