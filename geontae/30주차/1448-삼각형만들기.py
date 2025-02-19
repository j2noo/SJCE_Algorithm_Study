n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)
i = 0
j = 1
k = 2
while True:
    if arr[i] < arr[j] + arr[k]:
        print(arr[i] + arr[j] + arr[k])
        break
    k += 1
    if k == n:
        if arr[j] == arr[j+1]:
            j += 1
            k -= 1
        else:
            j += 1
            k = j + 1
    if j == n-1:
        if arr[i] == arr[i+1]:
            i += 1
            k -= 1
        else:
            i += 1
            j = i + 1
            k = j + 1
    if i == n-2:
        print(-1)
        break

