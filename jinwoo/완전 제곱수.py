import math
    
M=int(input())
N=int(input())

sum=0
minIdx=float("inf")

for i in range(1,101):
    if i*i>=M and i*i<=N:
        sum+=i*i
        minIdx = min(minIdx,i)

if sum==0:
    print(-1)
else :
    print(sum)
    print(minIdx*minIdx)
