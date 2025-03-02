# 정렬 먼저
# 4 8 13 24 30
# 8, 13을 찾기
# 9 10 11 12 중에 2개 고르기 4C2 - 여집합

L = int(input())
li = list(map(int, input().split()))
n = int(input())

li.sort()

s, e, exitFlag = -1, -1, 0
for item in li:
    if item < n:
        s = item
    if item > n and e == -1:
        e = item
    if item == n:
        exitFlag = 1

if exitFlag == 1:
    print(0)
    exit()

if s == -1:  # n이 가장작은숫자보다 작은 경우
    s = 0

# print("구간",s,e)
alls = (e - s - 1) * (e - s - 2) // 2
leftC = (n - s - 1) * (n - s - 2) // 2
rightC = (e - n - 1) * (e - n - 2) // 2

# print(all,leftC,rightC)
print(alls - leftC - rightC)
