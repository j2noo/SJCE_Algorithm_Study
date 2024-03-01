M = int(input())
N = int(input())
cnt = 0
min = 10000
for i in range(M, N+1):
    if i**(1/2) % 1 == 0:
        cnt += i
        if i < min:
            min = i
if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(min)
