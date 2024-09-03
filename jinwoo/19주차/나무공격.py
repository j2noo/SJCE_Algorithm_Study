import sys

n,m = map(int,input().split())
count_man = [-1]

for i in range(n):
    inp = input()
    count_man.append(inp.count("1"))
    
for _ in range(2):
    L,R = map(int,input().split())
    for i in range(L,R+1):
        count_man[i] -=1
# 세기
sum=0
for i in range(n+1):
    if count_man[i] > 0:
        sum+=count_man[i]
print(sum)

# 1 ~ 100번째 행이 공격당한 횟수 세기