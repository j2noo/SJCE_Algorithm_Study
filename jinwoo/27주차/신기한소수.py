# 99,999,999개의 소수 O(1)으로 파악
# 1부터 99999999까지 소수 구해서 해싱
# 소수판별이란
# n이 소수인지 판별 -> O(rootN)
# 1부터 n까지 소수 전부 구하기 -> O(N)?
# 1부터 root(N)까지 소수 구하고, 에라토스테네스의 체?

def isPrime(n):
    for i in range(2,(int)(n**0.5)+1):
        if n%i==0 : # 소수가 아님
            return False
    return True

# solve
N = int(input())
primes = [2,3,5,7]
odds = [1,3,5,7,9]
for _ in range(N-1):
    new_primes = []
    for prime in primes :
        for odd in odds:
            new_num = prime*10 +odd
            if isPrime(new_num):
                new_primes.append(new_num)
    primes = new_primes[:]
for prime in primes:
    print(prime)