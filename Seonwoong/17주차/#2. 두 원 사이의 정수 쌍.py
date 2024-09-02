import math
def solution(r1, r2):
    answer = 0

    for i in range(1,r2+1):
        start=0 if i>r1 else (r1*r1-i*i)**(1/2)
        end = (r2*r2-i*i)**(1/2)

        answer+=math.floor(end)+1 -math.ceil(start)

    answer=4*answer
    return answer
