n = int(input())
arr = [int(input()) for _ in range(n)]
res = []
arr.sort()

for i in range(1, n-1):
    res.append(((arr[i] - arr[i-1]) / 2) + ((arr[i+1] - arr[i]) / 2))

print(min(res))