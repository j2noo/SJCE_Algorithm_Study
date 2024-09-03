def solution(book_time):
    #사용시간을 0분(00:00)~1449분(23:59 + 10분)까지 저장할 리스트 
    usetime=[0]*(24*60+ 10)
    
    for i in book_time:
        #시작시간과 종료시간을 정수형으로 바꿔 저장, 종료시간에 10분(청소시간) 더해줘서 정수형 변환
        i[0]=int(i[0][0:2])*60+int(i[0][3:5])
        i[1]=int(i[1][0:2])*60+int(i[1][3:5])+10
        
    for i in book_time:
        #시작시간에서 종료시간까지 사용시간 기록
        for j in range(i[0],i[1]):
            if usetime[j]==0: usetime[j]=1
            else: usetime[j]+=1
   
    return max(usetime)
