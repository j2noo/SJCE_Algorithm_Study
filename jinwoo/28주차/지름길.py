# 2^12
from itertools import product, repeat


N,D = map(int,input().split())
yns = list(product(range(2),repeat=N))

infos = []
for _ in range(N):
    infos.append(list(map(int,input().split())))

infos.sort()

print(infos)
ans = 9878797
for yn in yns:
    pos = 0
    dist = 0
    for idx,val in enumerate(yn):
        if val==1: # 가자
            if infos[idx][1] > D : # 거리초과
                continue
                
            if pos <= infos[idx][0] : # 출발 가능
                dist += infos[idx][0] - pos + infos[idx][2] # 이동
                pos = infos[idx][1]
                
    dist += D  - pos + infos[idx][2]  # 이동
    print(yn,dist)
    ans = min(ans,dist)
print(ans)
        