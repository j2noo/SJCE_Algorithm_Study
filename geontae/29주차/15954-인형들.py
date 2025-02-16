import math

n, x = map(int, input().split())
arr = list(map(int, input().split()))
min = math.inf
for k in range(x, n+1):
    for i in range(n-k+1):
        m = sum(arr[i:i+k]) / k
        v = 0
        for j in range(i, i+k):
            v += (arr[j] - m) ** 2
        res = (v / k)**(0.5)
        if res < min:
            min = res
print(min)
