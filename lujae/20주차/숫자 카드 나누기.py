import math
# 시간 초과 ..
def get_max_answer(arrayA, arrayB):
    min_num = min(arrayA)

    for i in range(1, min_num // 2 + 1):
        if min_num / i < 1:
            break
        if min_num % i == 0:
            cri_num = min_num // i
            flag_fail = False

            for j in range(len(arrayA)):
                if arrayA[j] % cri_num != 0 or arrayB[j] % cri_num == 0:
                    flag_fail = True
                    break

            if not flag_fail:
                return cri_num

    return 0

def solution(arrayA, arrayB):
    return max(get_max_answer(arrayA, arrayB), get_max_answer(arrayB, arrayA))

print(solution([10, 17], [5, 20]))
