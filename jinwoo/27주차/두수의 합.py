from collections import defaultdict

n = int(input())
li  = list(map(int,input().split()))
x = int(input())
ans =0

dic = defaultdict(int)
for item in li :
    dic[item]=1
    
for item in li :
    cha = x - item
    # print(cha)
    if dic[cha]==1 :
        ans+=1
    # 0

print(ans//2)