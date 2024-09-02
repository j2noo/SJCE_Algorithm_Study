# 시간: 12분
# 스택

def solution(numbers):
    answer = [-1] * len(numbers)
    s = [(0, numbers[0])]

    for idx in range(1, len(numbers)):
        while s:
            topIdx, topNumber = s.pop()

            if topNumber < numbers[idx]:
                answer[topIdx] = numbers[idx]
            else:
                s.append((topIdx, topNumber))
                break

        s.append((idx, numbers[idx]))

    return answer