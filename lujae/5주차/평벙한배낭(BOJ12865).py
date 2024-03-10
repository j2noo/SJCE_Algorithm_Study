import sys

N, K = map(int, sys.stdin.readline().split(" "))
cache = [[0] * (K + 1) for i in range(N)]

arr = []

for i in range(N):
    W, V = map(int, sys.stdin.readline().split(" "))
    arr.append((W, V))


if arr[0][0] <= K:
    cache[0][arr[0][0]] = arr[0][1]

for i in range(1, N):
    w = arr[i][0]
    v = arr[i][1]

    for j in range(K + 1):
        cache[i][j] = max(cache[i][j], cache[i - 1][j])

        if j + w <= K:
            cache[i][j + w] = max(cache[i][j + w], cache[i - 1][j] + v)


print(max(cache[N - 1]))