# 50qns?
import sys
sys.setrecursionlimit(int(1e8))
def solution(n, l, r):
    answer = 0
    
    # 5^nn 크기를 가진 문자열의 [ll,rr] 내의 1의 개수
    def solve(nn,ll,rr):
        # base case
        if nn==1 :
            ret = 0
            for idx in range(ll,rr):
                if not idx==2:
                    ret+=1
            return ret
        
        # logic
        sum = 0
        for i in range(5):
            if i==2 :
                continue
            # [s,e)
            s = (5**nn) // 5 * i
            e = (5**nn) // 5 * (i+1) 
        
            # 올바르지 않은 구간
            if ll >= e:
                continue
            left = max(s,ll) - s
            
            if rr < s:
                continue
            right = min(e,rr) - s

            sum+=solve(nn-1,left,right)
        return sum
    # 폐구간을 반폐구간 [l,r+1)
    answer = solve(n,l-1,r)
        
    return answer

# 1
# 11011 [2.2]
# 1101111011000001101111011 [10,11,12,13,14] [10,15)
# ()()(00000)()()
# 단순 구현? -> 5^20 = 조 단위 X

# 1,5,25,125 ...
# n을 5등분할때, 가운데 구간은 전부 0이다.
# 그 등분 중에서, 가운데 구간은 0이다!
# 5^n, l, r 중 1의 개수를 반환하도록 하기