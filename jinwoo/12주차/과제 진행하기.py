from collections import deque
def solution(plans):
    start_sorted_li = []
    curIdx = 0
    stack = deque()
    answer = []
    for name,start,playtime in plans:
        hh,mm = map(int,start.split(':'))
        s =  hh*60 + mm
        e = s + int(playtime)
        
        start_sorted_li.append([s,e,name])
    start_sorted_li.sort()
    print(start_sorted_li)
    print()
    
    cur = []
    for t in range(1600):
        # 진행중인 일 1분 차감
        if cur :
            cur = [cur[0]-1,cur[1]]
            print("cur : ",cur)
            # 일이 끝남
            if cur[0] == 0:
                answer.append(cur[1])
                
                if stack :
                    cur = stack.popleft()
                else :
                    cur = []
                    
        if curIdx < len(plans)-1:
            nextJob = start_sorted_li[curIdx]
        
        # 일할시간!
        if t == nextJob[0] :
            curIdx+=1
            # 진행중인 일이 존재
            if cur:
                stack.append(cur)
                
            cur = [nextJob[e-s],name] # 남은시간, 이름
            print("@")
        
    return answer

# plans = input()/
plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
solution(plans)
