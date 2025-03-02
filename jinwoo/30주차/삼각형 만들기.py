# a + b > c(제일 긴 변)
# 10 4 3 2
# 10 7 3 2 2
# 앞에서 3개가 안되면? 123안되면 124도 안됨. 134도 안됨.
# 123, 234, 345
N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
li.sort(reverse=True)

for i in range(N-2):
    c = li[i]
    a, b = li[i+1:i+3]
    if c < a+b:
        print(a+b+c)
        exit()
print(-1)
# 10분