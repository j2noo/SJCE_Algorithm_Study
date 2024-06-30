# 시간 : 5분50초
# Lv : 1

def solution(name, yearning, photo):
    dic = {}
    for i in range(len(name)):
        dic[name[i]] =yearning[i]
    
    answer=[]
    for ph in photo:
        sum=0
        for each_name in ph:
            if each_name in dic:
                sum+=dic[each_name]
        answer.append(sum)
        
    return answer

# 파이썬 개사기. 문법 몰라도 이게되네 