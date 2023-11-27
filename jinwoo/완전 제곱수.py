import math

powerArr = []
for i in range(101):
    powerArr.append(i*i)
    
M=int(input())
N=int(input())

startIdx = math.ceil(math.sqrt(M))
endIdx =math.floor(math.sqrt(N))


sum=0
for i in range(startIdx,endIdx+1):
    sum+=powerArr[i]
    
if startIdx>endIdx:
    print(-1)

else :
    print(sum)
    print(powerArr[startIdx])