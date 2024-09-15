# 4분
# 레벨2 개쉽다
# 브론즈1

import sys
n = int(input())
rad_li = list(map(int,input().split()))

ans = -1
for len in range(2,101):
    cnt=0
    for r in rad_li:
        if r % len == 0:
            cnt+=1
    ans=max(ans,cnt)
print(ans)