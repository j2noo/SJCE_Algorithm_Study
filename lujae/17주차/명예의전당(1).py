# 시간: 8분
# 풀이: 힙

import heapq

def solution(k, score):
    answer = []

    h = []
    for s in score:
        if len(h) < k:
            heapq.heappush(h, s)
        else:
            if s > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, s)

        answer.append(h[0])


    return answer