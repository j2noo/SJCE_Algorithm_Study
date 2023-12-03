import math

M = int(input())
N = int(input())
squareNumber = []

for i in range (M, N + 1):
    if math.sqrt(i) == i // math.sqrt(i):
        squareNumber.append(i)

sum = 0
for i in range (len(squareNumber)):
    sum += squareNumber[i]

if sum != 0:
    print(sum)
    print(min(squareNumber))
else:
    print(-1)