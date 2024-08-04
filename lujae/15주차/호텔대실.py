# 시간: 30분
# 정렬, 구현 => nlogn 풀이 방법은 없나
def convertTime(time):
    h, m = map(int, time.split(":"))

    return 60 * h + m

def solution(book_time):
    answer = 0

    btConverted = []

    for bt in book_time:
        btConverted.append((convertTime(bt[0]), convertTime(bt[1]) + 10))

    btConverted.sort(key = lambda x : (x[1], x[0]))

    # idx = 1
    # criterionTime = (btConverted[0][0], btConverted[0][1])
    # needRoomCnt = 1
    #
    # while idx < len(btConverted):
    #     if criterionTime[1] <= btConverted[idx][0]:
    #         criterionTime = (btConverted[idx][0], btConverted[idx][1])
    #         needRoomCnt = 1
    #     else:
    #         needRoomCnt += 1
    #
    #     answer = max(answer, needRoomCnt)
    #     idx += 1

    # 2중 반복문인데 1중으로 줄이는 방법은 없을까
    for i in range(len(btConverted)):
        needRoomCnt = 1
        for j in range(i + 1, len(btConverted)):
            if btConverted[i][1] > btConverted[j][0]:
                needRoomCnt += 1

        answer = max(answer, needRoomCnt)

    return answer