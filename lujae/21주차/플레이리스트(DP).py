def sol(cache, here, N, P, K, li, usedMaxNum):
    if here == P:
        if usedMaxNum == N:
            return 1
        else:
            return 0

    if cache[here][usedMaxNum] != -1:
        return cache[here][usedMaxNum]

    cnt_used_number = usedMaxNum
    cnt_rest_number = N - cnt_used_number

    end = max(0, here - 1)
    start = max(0, end - (K - 1))

    overlap_number_set = set(li[start:end + 1])
    not_overlap_number = -1

    for i in range(1, usedMaxNum + 1):
        if i not in overlap_number_set:
            not_overlap_number = i
            break

    # case1 여태까지 한 번도 사용 x
    case1_ret = 0
    if cnt_rest_number > 0:
        li.append(usedMaxNum + 1)
        tmp = sol(cache, here + 1, N, P, K, li, usedMaxNum + 1)
        case1_ret = cnt_rest_number * tmp % MOD
        li.pop()

    # case2 사용했지만 그룹에 없는 수
    case2_ret = 0
    if not_overlap_number != -1:
        li.append(not_overlap_number)
        tmp = sol(cache, here + 1, N, P, K, li, usedMaxNum )
        case2_ret = (usedMaxNum - len(overlap_number_set)) * tmp % MOD

        li.pop()

    cache[here][usedMaxNum] = (case1_ret + case2_ret) % MOD
    return cache[here][usedMaxNum]

N, M, P = map(int, input().split())
MOD = 1000000007

cache = [[-1] * (N + 1) for i in range(P + 1)]
ret = sol(cache, 0, N, P, M, [], 0) % MOD

print(ret)