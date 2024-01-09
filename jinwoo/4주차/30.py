N = list(map(int,input()))
N.sort()
if sum(N)%3 != 0 or N[0]!=0:
    print(-1)
    exit(0)
N.reverse()
for i in N:
    print(i,end="")