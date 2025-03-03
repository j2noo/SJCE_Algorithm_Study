n = int(input())
arr = list(map(int, input().split()))
res = [-1] * n
for i in range(0, n):
    cnt = 0
    j = 0
    while True:
        if res[j] == -1:
            if cnt == arr[i]:
                res[j] = i + 1
                break
            cnt += 1
            j += 1
        else:
            j += 1

for i in range(n):
    print(res[i], end=" ")

# 빈자리가 arr[i]만큼 세고 넣기