## 11011
## 11011 11011 00000 11011 11011

def check(i):
    # i가 5로 나눈 나머지가 2인 경우 (0-based 인덱스에서 '0'으로 간주)
    if i % 5 == 2:
        return False
    # i가 5보다 작은 경우 (0, 1, 3, 4는 '1'로 간주)
    if i < 5:
        return True
    # 재귀적으로 5로 나누어 값 계산
    return check(i // 5)

def solution(n, l, r):
    answer = 0

    for i in range(l - 1, r):  # l과 r은 1-base이므로 0-base로 변환
        if check(i):
            answer += 1

    return answer
