## dp


def func(cache, apache_state, restCnt, here, backTrack):
    if here == 11:
        return 0

    if cache[here][restCnt] != -1:
        return cache[here][restCnt]

    ret = 0
    for cnt in range(0, restCnt + 1):
        score = 0

        if cnt > apache_state[here]:
            score = here

        if apache_state[here] >= 1:
            score *= 2

        tmp_ret = score + func(cache, apache_state, restCnt - cnt, here + 1, backTrack)
        if ret <= tmp_ret:
            ret = tmp_ret
            backTrack[here][restCnt] = cnt

    cache[here][restCnt] = ret
    return ret

def solution(n, info):
    answer = []

    new_info = [info[10 - i] for i in range(11)]
    apache_score = 0
    cache = [[-1] * 11 for _ in range(11)]
    backTrack = [[-1] * 11 for _ in range(11)]

    for score in range(11):
        if new_info[score] > 0:
            apache_score += score

    ret = func(cache, new_info, n, 0, backTrack)

    if apache_score >= ret:
        return [-1]

    rest_cnt = n
    for here in range(11):
        use_cnt = backTrack[here][rest_cnt]
        answer.append(use_cnt)
        rest_cnt -= use_cnt

    answer.reverse()
    return answer