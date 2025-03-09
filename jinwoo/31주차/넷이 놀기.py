# 500000 C 4 -> x
# {x : val} 으로 가지는 map
# {x : val+size} 가 있는지 체크 -> O(1)

from collections import defaultdict

dict = defaultdict(int)
ans = 0

N = int(input())
A,B = map(int,input().split())
for _ in range(N):
    x,y = map(int,input().split())
    dict[(x,y)] +=1

for item in list(dict) :
    x,y = item
    ans += dict[(x+A,y)] * dict[(x,y+B)] * dict[(x+A,y+B)]
print(ans)