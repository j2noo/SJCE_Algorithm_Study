# mid에서 ㅂ블루레이 그거 가능하한지 체크
def check(mid):
    sum=0
    cnt=1 # 마지막이 mid보다 크면어케
    for lesson in lessons :
        if lesson >mid:
            return False
        
        if sum + lesson <= mid : # 블루레이에 담김
            sum+=lesson
        else :
            sum=lesson
            cnt+=1
            if cnt>M:
                # print(f'mid : {mid}, cnt : {cnt} x')
                return False
    
    if cnt<=M :
        # print(f'mid : {mid}, cnt : {cnt} o')
        return True
            
            

N,M = map(int,input().split()) 

lessons = list(map(int,input().split()))
# lessons.sort()

# N = 100000
# M=1
# lessons = [1]*100000

lo,hi = 0,100_000_000_9 # 강의의 길이

while lo+1<hi :
    mid = (lo+hi)//2
    if check(mid) == check(lo):
        lo = mid
        # print(f'mid : {mid}, [{lo,hi}]1')
    else:
        hi = mid
        # print(f'mid : {mid}, [{lo,hi}]2')
    # print()

print(hi)

