import math


def to_digit(n, k):
    res = []

    while n:
        res.insert(0, n % k)
        n = n // k
    return res


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    digit = to_digit(n, k)
    digit.append(0)
    tmp = []
    for i in range(0, len(digit)):
        if digit[i] == 0:
            if tmp and is_prime(int("".join(map(str, tmp)))):
                answer += 1
            tmp = []
        else:
            tmp.append(digit[i])
    return answer
