def solution(k, d):
    answer = 0 
    for x in range(0,d+1,k):
        y=int((d*d-x*x)**(1/2))
        answer+=y//k+1

    return answer
