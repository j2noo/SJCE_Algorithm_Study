import sys
input=sys.stdin.readline
N = int(input().strip())            
arr = list(map(int, input().split()))
answer=[0]*N

for i, height in enumerate(arr):
    count = 0
    for j, res in enumerate(answer):
        if res==0 and count<height:
            count+=1
        elif res==0 and count==height:
            answer[j]=i+1
            break

print(*answer)