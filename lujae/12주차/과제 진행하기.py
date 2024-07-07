# 32분 11초

# t의 범위를 엄청크게 설정하니까 통과함
# "00:00" ~ "23:59" 사이의 시간값만 들어가 있습니다. 인데 t의 범위는 0 ~ 1440이 아닌가 ?? 어이없네

import collections

def timeConvertor(time):
    (h, m) =  map(int, time.split(":"))
    return h * 60 + m

def solution(plans):
    answer = []
    plans.sort(key = lambda x : x[1])
    
    for i in range(len(plans)):
        plans[i][1] = timeConvertor(plans[i][1])
        plans[i][2] = int(plans[i][2])
    
    TaskWaitQueue = collections.deque()
    idx = 0
    
    currentTask = 0
    for t in range(plans[0][1], 6000 * 24 + 102):
        if idx + 1 < len(plans) and plans[idx + 1][1] == t:
            if plans[currentTask][2] != 0:
                TaskWaitQueue.append(currentTask)
            
            currentTask = idx + 1
            idx += 1
        elif plans[currentTask][2] == 0:
            if TaskWaitQueue:
                currentTask = TaskWaitQueue.pop()

        if plans[currentTask][2] > 0:
            plans[currentTask][2] -= 1
            if plans[currentTask][2] == 0:
                print("*** [end] Time: %d, TaskName = %s ***" %(t, plans[currentTask][0]))
                answer.append(plans[currentTask][0])

    return answer

plans = [["a", "09:00", "30"], ["b", "09:20", "10"], ["c", "09:40", "10"]]

print(solution(plans))