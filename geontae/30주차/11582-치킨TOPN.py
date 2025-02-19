n = int(input())
arr = list(map(int, input().split()))
k = int(input())
m = 2
while True:
    n = n//2
    i = 0
    for _ in range(n):
        arr[i:i+m] = sorted(arr[i:i+m])
        i += m
    m *= 2
    if n == k:
        break
for i in range(len(arr)):
    print(arr[i], end=' ')