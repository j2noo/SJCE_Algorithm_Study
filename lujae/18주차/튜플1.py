## 시간: 17분
## 풀이: 문자열 나누기 + 딕셔너리
def get_set_list(s):
    s = s[1:-1]
    ret = []
    idx = 0

    while idx < len(s):
        if s[idx] == ',':
            idx += 1
            continue
        elif s[idx] == '{':
            end_idx = idx
            while end_idx < len(s) and s[end_idx] != '}':
                end_idx += 1

            ret.append(list(map(int, s[idx + 1: end_idx].split(","))))
            idx = end_idx + 1
    ret.sort(key=lambda x: len(x))
    return ret

def solution(s):
    answer = []
    emerge_number = dict()

    set_list = get_set_list(s)
    for set in set_list:
        for num in set:
            if num not in emerge_number:
                emerge_number[num] = True
                answer.append(num)
                break

    return answer