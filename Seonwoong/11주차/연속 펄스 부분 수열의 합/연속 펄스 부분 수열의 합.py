from itertools import accumulate

def solution(sequence):
    n = len(sequence)
    pulse = [((-1)**(i%2))*sequence[i] for i in range(n)]
    repulse = [i*(-1) for i in pulse]
    
    arr = []
    arr.append(list(accumulate(pulse, lambda x, y:max(y,x+y))))
    arr.append(list(accumulate(repulse, lambda x, y:max(y, x+y))))
    
    answer = max(max(arr[0]), max(arr[1]))
    return answer
