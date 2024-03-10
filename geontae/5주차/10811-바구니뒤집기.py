n, m = map(int, input().split())
arr = []
arr.append(0)
for i in range(1, n+1):
    arr.append(i)
#print(arr)
for _ in range(m):
    i, j = map(int, input().split())
    while True:
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

print(*arr[1:n+1])