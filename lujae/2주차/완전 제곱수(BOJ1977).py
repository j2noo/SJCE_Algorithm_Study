import math

M = int(input())
N = int(input())

start = int(math.sqrt(M))
end = int(math.sqrt(N))

powSum = 0
powMin = 10000000

for i in range(start, end + 1):
    pow = i ** 2
    if(pow >= M and pow <= N):
        powMin = min(powMin, pow)
        powSum += pow

if(powSum == 0):
    print(-1)
else:
    print(powSum)
    print(powMin)