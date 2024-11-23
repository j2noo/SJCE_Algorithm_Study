# N^2, 두 원소를 뺸 100만개짜리 배열을 만듦.
# n^2, 두 원소를 더했을 때 100만개짜리 해시에 존재하면 -> 만들 수 있음
from collections import defaultdict

N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
cha_dic = defaultdict(list)

li.sort()

for i in range(N):
    for j in range(i, N):
        cha_dic[abs(li[i] - li[j])].append([li[i], li[j]])

# {1: 0, 3: 0, 8: 0, 16: 0, 2: 0, 7: 0, 15: 0, 5: 0, 13: 0})
# 두 개 더해서 이걸 만들수 있으면 됨.
ans = -1

for i in range(N):
    for j in range(i, N):
        sum = li[i] + li[j]
        if len(cha_dic[sum]) > 0:  # 있다!
            for s1, s2 in cha_dic[sum]:
                ans = max(s2, ans)
print(ans)
