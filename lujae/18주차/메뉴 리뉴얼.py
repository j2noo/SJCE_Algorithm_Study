# 시간 40분
# 구현

import itertools
def solution(orders, course):
    answer = []
    checked = {}
    bit_mask = {}

    for i in range(len(orders)):
        orders[i] = "".join(sorted(orders[i]))
    orders.sort(key = lambda x : len(x))


    for order in orders:
        num = 0

        for ch in order:
            idx = ord(ch) - ord('A')

            num += 2 << idx

        bit_mask[order] = num

    for cnt in course:
        combination_str_list = []

        for order in orders:
            combinations = itertools.combinations(order, cnt)

            for combination in combinations:
                combi_join = "".join(combination)

                if combi_join not in checked:
                    combination_str_list.append(combi_join)
                    checked[combi_join] = True

        str_emerge_cnt_map = {}
        for combination_str in combination_str_list:
            emerge_cnt = 0

            for order in orders:
                if len(combination_str) > len(order):
                    continue

                num = 0

                for ch in combination_str:
                    idx = ord(ch) - ord('A')

                    num += 2 << idx

                if bit_mask[order] & num == num:
                    emerge_cnt += 1

            str_emerge_cnt_map[combination_str] = emerge_cnt

        if len(str_emerge_cnt_map) != 0:
            max_emerge_cnt = max(str_emerge_cnt_map.values())

            if max_emerge_cnt >= 2:
                for key in str_emerge_cnt_map:
                    if str_emerge_cnt_map[key] == max_emerge_cnt:
                        answer.append(key)

    return sorted(answer)