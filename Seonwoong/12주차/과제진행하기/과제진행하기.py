def solution(plans):
    answer=[]
    now=[]
    #배열 시간순으로 정렬
    #배열 수정: 시간을 모두 분으로 수정, 문자형 정수를 정수형으로 수정
    plans.sort(key=lambda x:x[1])
    for i in range(len(plans)):
        plans[i][1]=int(plans[i][1][0:2])*60+int(plans[i][1][3:])
        plans[i][2]=int(plans[i][2])
    
    for i in range(len(plans)-1):
        #현재과제와 다음과제 차이 계산
        now.append(plans[i])
        diff=plans[i+1][1]-plans[i][1]
        
        #시간차이가 업거나 진행중인 과제가 없을때까지 반복
        while now and diff:
            #현재과제 해결 가능: 완료리스트(answer)에 추가, 진행중과제 pop
            if now[-1][2]<=diff:
                diff-=now[-1][2]
                answer.append(now[-1][0])
                now.pop()
            #현재과제 해결 불가능: 진행중인 과제에 시간차이 업데이트
            else: 
                now[-1][2]-=diff
                diff=0
    
    #마지막과제와 남아있는 진행중인 과제 역순으로 저장
    answer.append(plans[-1][0])
    while now:
        answer.append(now[-1][0])
        now.pop(-1)
    
    return answer

# 약 한시간 정도 소요
# 시간복잡도 O(n*logn)
