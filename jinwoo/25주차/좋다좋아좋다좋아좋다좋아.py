from collections import defaultdict
N = int(input())
numbers = list(map(int,input().split()))

answer=0
numbers.sort()


for idx,val in enumerate(numbers):
    # val이 좋은 수인지 찾기
    s,e = 0,N-1
    while s < e :
        sum = numbers[s]+numbers[e]
        if sum < val :
            s+=1
        elif sum > val:
            e-=1
        else :
            if s == idx:
                s+=1
            elif e == idx:
                e-=1
            else:
                answer+=1
                break
 



print(answer)
    