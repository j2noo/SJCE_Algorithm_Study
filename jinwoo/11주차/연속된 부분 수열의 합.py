# 1시간..
# lv v2


def solution(sequence, k):

    # psum[i] : i번째 인덱스까지의 누적합d

    psum=[0]
    sum=0
    ans_li = []
    min_len = 987654321
    for i in sequence:
        sum+=i
        psum.append(sum)

    # idx를 start로 하는 구간 찾기
    for i in range(len(sequence)):
        # psum[end+1] = target인 end 찾기
        start = i
        target = psum[i] +k
        
        
        lo = i
        hi=len(sequence)+1
        while(lo+1<hi):
            mid = (lo+hi)//2
            if psum[mid] <=target :
                lo = mid
            else :
                hi = mid
        
        # print("s,e",start,lo,"target :",target)
        if psum[lo]==target:
            # print("s,e",start,lo,"target :",target)
            # print("@",i,start-1)
            if lo-start-1 < min_len: 
                ans_li.append([start,lo-1])
                min_len =lo-start-1  
    # for i in ans_li:
    #     print(i)
    return ans_li[-1]

#psum 배열이 존재.
# 각 idx(start)에 대해, 합이 k가되는  end를 이분탐색

# psum : 0 1 3 6 10 15
# sum = p[4]-p[2], (2,3)