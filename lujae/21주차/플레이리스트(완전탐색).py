## 현재 코드의 문제점 => K의 값이 같은 경우에 대해서는 중복이 발생하지 않지만, 서로 다른 K일 경우의 수 일때는 중복이 발생할 수 있음
## 조금 더 추상화된 방식을 생각해야함 !
## 현재 코드의 시간복잡도는 ? O(2^N)
def sol(here, N, P, K, li, usedMaxNum):
    if here == P:
        if usedMaxNum == N:
            return 1
        else:
            return 0

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
        tmp = sol(here + 1, N, P, K, li, usedMaxNum + 1)
        case1_ret = cnt_rest_number * tmp % MOD
        li.pop()

    # case2 사용했지만 그룹에 없는 수
    case2_ret = 0
    if not_overlap_number != -1:
        li.append(not_overlap_number)
        tmp = sol(here + 1, N, P, K, li, usedMaxNum )
        case2_ret = (usedMaxNum - len(overlap_number_set)) * tmp % MOD

        li.pop()

    return (case1_ret + case2_ret) % MOD

N, M, P = map(int, input().split())
MOD = 1000000007

ret = sol(0, N, P, M, [], 0) % MOD

print(ret)