def solution(id_list, report, k):
    id_idx = {}
    report_idx = {}
    report = list(set(report))

    for i in range(0, len(id_list)):
        id_idx[id_list[i]] = 0
        report_idx[id_list[i]] = 0
    for i in range(0, len(report)):
        a, b = report[i].split()
        report_idx[b] += 1
    for i in range(0, len(report)):
        a, b = report[i].split()
        if report_idx[b] >= k:
            id_idx[a] += 1

    answer = list(id_idx.values())
    return answer
