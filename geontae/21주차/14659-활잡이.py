n = int(input()) + 1
arr = list(map(int, input().split()))
arr.append(100001)
res = 0
cnt = 0
start = arr[0]
for i in range(1, n):
    if arr[i] < start:
        cnt += 1
    else:
        start = arr[i]
        if res < cnt:
            res = cnt
        cnt = 0
print(res)
