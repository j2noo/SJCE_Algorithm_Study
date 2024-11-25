import collections
def convertTime(str_time):
    h, m = map(int, str_time.split(":"))
    return h * 60 + m

def cal_fee(fees, time):
    if time <= fees[0]:
        return fees[1]

    time -= fees[0]
    factor = time // fees[2]
    if time % fees[2] != 0:
        factor += 1

    return fees[1] + factor * fees[3]
def solution(fees, records):
    answer = []

    dict_time_in = {}
    dict_car_fee = collections.defaultdict(int)
    dict_car_total_time = collections.defaultdict(int)

    for record in records:
        str_time, car_number, dir = record.split(" ")
        current_time = convertTime(str_time)

        if dir == "IN":
            dict_time_in[car_number] = current_time
        else:
            before_time = dict_time_in[car_number]
            diff_time = current_time - before_time
            dict_car_total_time[car_number] += diff_time
            dict_time_in[car_number] = -1

    for key in dict_time_in.keys():
        current_time = convertTime("23:59")

        if dict_time_in[key] != -1:
            before_time = dict_time_in[key]
            diff_time = current_time - before_time
            dict_car_total_time[key] += diff_time
            dict_time_in[key] = -1

    for key in dict_car_total_time.keys():
        dict_car_fee[key] = cal_fee(fees, dict_car_total_time[key])

    for key in sorted(dict_car_fee.keys()):
        answer.append(dict_car_fee[key])

    return answer