# 시간 10분
# 1트

import collections
def solution(id_list, report, k):
    answer = []

    dic_target_set = {}
    dic_report_cnt = collections.defaultdict(int)

    for id in id_list:
        dic_target_set[id] = set()

    for r in report:
        p1, p2 = r.split(" ")

        if p2 not in dic_target_set[p1]:
            dic_target_set[p1].add(p2)
            dic_report_cnt[p2] += 1

    for id in id_list:
        tmp_ret = 0

        for target in dic_target_set[id]:
            if dic_report_cnt[target] >= k:
                tmp_ret += 1

        answer.append(tmp_ret)

    return answer