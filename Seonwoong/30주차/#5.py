from itertools import combinations

A = int(input())
B = int(input())

rounds = [i for i in range(1, 90 // 5 + 1)]
primes = [2, 3, 5, 7, 11, 13, 17]

pA = A / 100.0
qA = 1 - pA

pB = B / 100.0
qB = 1 - pB

sumA = 0
sumB = 0

for i in range(len(primes)):

    comb = len(list(combinations(rounds, primes[i])))
    sumA += comb * (pA**primes[i]) * (qA**(18-primes[i]))
    sumB += comb * (pB**primes[i]) * (qB**(18-primes[i]))

print(sumA +sumB - sumA*sumB)