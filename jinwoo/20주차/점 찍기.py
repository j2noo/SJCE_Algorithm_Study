# 10분
def solution(k, d):
    answer = 0
    
    for x in range(0,d+1,k):
        max_y = int((d**2 - x**2)**0.5)
        answer+=(max_y // k)+1
        
    return answer

# 반지름이 d인 원?
# x가 0부터 d까지,가능한 y의 값 개수 세기