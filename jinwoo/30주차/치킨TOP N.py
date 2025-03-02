# n logn 병합정렬?
# 8분
N = int(input())
li = list(map(int,input().split()))
k = int(input())

length = N//k

tmp = []
for idx,val in enumerate(li) :
    if idx % length == 0 and idx!=0 :
        tmp.sort()
        for item in tmp :
            print(item,end=" ")
        tmp = []
    tmp.append(val)
tmp.sort()
for item in tmp:
    print(item,end=" ")