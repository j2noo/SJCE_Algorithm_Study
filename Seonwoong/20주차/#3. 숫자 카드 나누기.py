import math
from functools import reduce

def can_divide_all(gcd, array):
    return all(x % gcd == 0 for x in array)

def cannot_divide_any(gcd, array):
    return any(x % gcd == 0 for x in array)

def solution(arrayA, arrayB):
    # 철수와 영희의 카드에 대한 최대 공약수 계산
    A_gcd = reduce(math.gcd, arrayA)
    B_gcd = reduce(math.gcd, arrayB)

    answer = []
    
    # 조건 1: A_gcd가 B의 모든 숫자를 나누지 않아야 함
    if not can_divide_all(A_gcd, arrayB) and not cannot_divide_any(A_gcd, arrayB):
        answer.append(A_gcd)
    # 조건 2: B_gcd가 A의 모든 숫자를 나누지 않아야 함
    if not cannot_divide_any(B_gcd, arrayA) and not can_divide_all(B_gcd, arrayA):
        answer.append(B_gcd)
        
    # 결과 반환
    return max(answer) if answer else 0
