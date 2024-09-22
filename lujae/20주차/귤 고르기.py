# 시간: 6분
# 구현

import collections
def solution(k, tangerine):
    answer = 0
    total_cnt = 0

    for item in collections.Counter(tangerine).most_common(len(tangerine)):
        answer += 1
        total_cnt += item[1]

        if total_cnt >= k:
            break

    return answer