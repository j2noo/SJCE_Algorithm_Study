import math
N =input()
li = list(map(int,N))
N=int(N)
# print(li)

# 중복 제거 set
s = set(li)
lcm = 1
for num in s:
    if num!=0:
        lcm = math.lcm(lcm,num)
# print("set : ",s,"lcm : ",lcm)

# lcm로 나누면 됨, N에다가 하나씩 수를 붙여서 계산
if N%lcm ==0:
    print(N)
    exit()

expo = 1
while(1):
    maxNum = 10**expo
    for i in range(maxNum):
        newNum = N*maxNum + i
        if newNum % lcm ==0:
            print(newNum)
            exit()
    expo+=1
# print("꺼져")         
