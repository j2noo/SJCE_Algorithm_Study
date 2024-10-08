from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    carNum = [] # 차량 번호 리스트
    carTime = defaultdict(list) # 차량별 시간. 리스트 형으로 초기화
    
    for i in range(0, len(records)):
        carNum.append(records[i][6:10])
        carTime[records[i][6:10]] += [int(records[i][0:2])*60+int(records[i][3:5])]
    
    carNum = list(set(carNum))
    carNum.sort()
    
    for i in range(0, len(carTime)): # 순서대로 출력해봄
        if len(carTime.get(carNum[i])) % 2 != 0:
            carTime.get(carNum[i]).append('1439') # 출차시간 없으면 23:59
        sum = 0
        for j in range(0, len(carTime.get(carNum[i]))-1,2): 
            diff = int(carTime.get(carNum[i])[j+1])-int(carTime.get(carNum[i])[j])

            sum += diff 
        
        if sum <= fees[0] :
            answer.append(fees[1])
        else :
            answer.append(fees[1] + math.ceil((sum-fees[0])/fees[2]) *fees[3])
        
    return answer


