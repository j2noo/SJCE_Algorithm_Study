# 시간 30분
# 점수 40점

import collections
import heapq
def solution(k, n, reqs):
    answer = 0

    mentor_list = [i for i in range(1, k + 1)]
    rest_mentor_cnt = n - k

    reqs.sort(key = lambda x : (x[0], x[1]))
    reqs_idx = 0
    wait_queue = collections.deque()
    total_wait_queue = collections.deque()
    task_queue = []

    for t in range(1, 300 * 100 + 1000):
        if reqs_idx == len(reqs) and len(wait_queue) == 0 and len(task_queue) == 0:
            break

        now_append_mentor_list = []
        while len(task_queue) != 0 and task_queue[0][0] == t:
            completed_task = heapq.heappop(task_queue)
            mentor_list.append(completed_task[1])
            now_append_mentor_list.append(completed_task[1])

        if len(wait_queue) != 0 and len(now_append_mentor_list) != 0:
            delete_element_list = []

            for e in wait_queue:
                if e[0] in mentor_list:
                    type = e[0]
                    answer += t - e[1]
                    end_time = t + e[2]

                    delete_element_list.append(e)
                    mentor_list.remove(type)
                    heapq.heappush(task_queue, (end_time, type))

            for de in delete_element_list:
                total_wait_queue.append((de[0], de[1], t)) # (유형, 기다리기 시작한 시점, 기다림이 끝난 시간)
                wait_queue.remove(de)

        if reqs_idx < len(reqs) and t == reqs[reqs_idx][0]:
            type = reqs[reqs_idx][2]
            end_time = t + reqs[reqs_idx][1]

            if type in mentor_list:
                mentor_list.remove(type)
                heapq.heappush(task_queue, (end_time, type))
            elif rest_mentor_cnt >= 1:
                rest_mentor_cnt -= 1
                heapq.heappush(task_queue, (end_time, type))
            else:
                wait_queue.append((type, t, reqs[reqs_idx][1]))

            reqs_idx += 1

    ## 기다려야 했던 상담에 멘토 추가 배정
    # used_time_range_by_type = [range(0, 1)] * (k + 1)
    # additional_mentor_cnt = [0] * (k + 1)
    #
    # total_wait_queue = collections.deque(sorted(total_wait_queue, key= lambda x : (-(x[2] - x[1]), x[1])))
    #
    # while rest_mentor_cnt >= 1 and len(total_wait_queue) != 0:
    #     te = total_wait_queue.popleft()
    #
    #     type = te[0]
    #     start_wait_time = te[1]
    #     end_wait_time = te[2]
    #     used_time = end_wait_time - start_wait_time
    #
    #     if additional_mentor_cnt[type] >= 1:
    #         if end_wait_time in used_time_range_by_type[type]:
    #             rest_mentor_cnt -= 1
    #             used_time_range_by_type[type] = range(start_wait_time, end_wait_time)
    #             additional_mentor_cnt[type] += 1
    #         else:
    #             used_time_range_by_type[type] = range(start_wait_time, end_wait_time)
    #     else:
    #         rest_mentor_cnt -= 1
    #         used_time_range_by_type[type] = range(start_wait_time, end_wait_time)
    #         additional_mentor_cnt[type] += 1
    #
    #     answer -= used_time

    return answer

print(solution(		3, 5, [[10, 100, 1], [20, 100, 1], [30, 100, 1], [40, 100, 1]]))