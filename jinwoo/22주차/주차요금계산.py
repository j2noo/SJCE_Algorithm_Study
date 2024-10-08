def solution(fees, records):
    infos = {}
    moneys = {}
    for record in records :
        time, number, type = record.split()
        if number in infos :
            infos[number].append([time,type])
        else :
            infos[number] = [[time,type]]
            moneys[number]=0

    
    for number, val in infos.items():
        if len(val)%2 == 1 :
            val.append(["23:59","OUT"])
        for i in range(len(val)//2):
            sh, sm = map(int,val[i*2][0].split(':'))
            eh, em = map(int,val[i*2+1][0].split(':'))
            
            existTime = (eh*60 + em) - (sh*60+sm)
            moneys[number]+=existTime
            
    answer = []
    for number, val in moneys.items():
        
        if val <= fees[0]:
            money = fees[1]
        else :
            money = fees[1] +( (val-fees[0] + fees[2]-1)//fees[2]) * fees[3]
        moneys[number]=money
    
    sortedKey = list(moneys.keys())
    sortedKey.sort()
    for key in sortedKey:
        answer.append(moneys[key])
    return answer