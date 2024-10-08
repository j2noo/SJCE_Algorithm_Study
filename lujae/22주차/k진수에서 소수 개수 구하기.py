import math
## 소수인지 아닌지 판단하는 거를 어떻게 최적화 하지 ?
## 20억
## 20분

def convert(n, k):
    ret = ""

    while n >= k:
        r = n % k
        n = n // k

        ret = str(r) + ret
        if n < k:
            ret = str(n) + ret

    return ret

def isPrime(n):
    if n <= 1:
        return False

    for num in range(2, int(math.sqrt(n)) + 1):
        if n % num == 0:
            return False

    return True

def solution(n, k):
    answer = 0

    str_list = convert(n, k).split("0")

    for st in str_list:
        if st != "":
            if isPrime(int(st)):
                  answer += 1

    return answer