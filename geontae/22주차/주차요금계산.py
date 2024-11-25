import math


def solution(fees, records):
    answer = []
    fee = {}
    time_table = {}
    for i in range(0, len(records)):
        time, num, p_type = records[i].split()
        if p_type == 'IN':
            time_table[num] = time
        else:
            o_time = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
            i_time = int(time_table[num].split(":")[0]) * 60 + int(time_table[num].split(":")[1])
            if num in fee:
                fee[num] += o_time - i_time
            else:
                fee[num] = o_time - i_time
            time_table[num] = 0

    for key in time_table:
        if time_table[key] != 0:
            if key in fee:
                fee[key] += 1439 - (int(time_table[key].split(":")[0]) * 60 + int(time_table[key].split(":")[1]))
            else:
                fee[key] = 1439 - (int(time_table[key].split(":")[0]) * 60 + int(time_table[key].split(":")[1]))

    sorted_values = [fee[key] for key in sorted(fee)]

    for v in sorted_values:
        x = fees[1] + math.ceil((v - fees[0]) / fees[2]) * fees[3]
        if x <= fees[1]:
            answer.append(fees[1])
        else:
            answer.append(x)
    
    return answer
