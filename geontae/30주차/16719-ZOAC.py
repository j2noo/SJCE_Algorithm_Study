# 끝이면 리턴, 앞에 모든걸 프린트햇으면 리턴
# 아니면 프린트 한거 제외하고 가장 앞에꺼 출력
# 기준 문자가 있음

s = input()
n = len(s)
is_printed = [0] * n
def sol(is_printed, i):
    while True:
        min_str = '{'
        min_idx = 0
        f = 0
        for k in range(i, n):
            if s[k] < min_str and is_printed[k] == 0:
                min_str = s[k]
                min_idx = k
                f = 1
        if f == 1:
            is_printed[min_idx] = 1
            for j in range(n):
                if is_printed[j] == 1:
                    print(s[j], end="")
            print()
            sol(is_printed, min_idx)
        else:
            break
    return 0

sol(is_printed, 0)