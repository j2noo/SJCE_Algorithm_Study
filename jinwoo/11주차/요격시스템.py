# 1시간 고민하다 안풀려서 풀이봄
# https://school.programmers.co.kr/questions/47317
# 레벨2 이거맞냐?;;
# 가장 많이 겹치는 곳을 쏘는거라고생각
def solution(targets):
    targets.sort()
    # print(targets)
    cnt = 0
    s,e = targets[0]
    for i in range(len(targets)):
        
        if targets[i][0] >= e:
            # print("cnt")
            cnt+=1
            
            s,e = targets[i]
            continue;
                
        s=targets[i][0]
        e = min(e,targets[i][1])
        # print("s,e",s,e)
    return cnt+1