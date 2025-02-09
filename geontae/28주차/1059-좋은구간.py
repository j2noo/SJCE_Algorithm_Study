L = int(input())
arr = list(map(int, input().split()))
n = int(input())

arr.sort()
start = 0
end = 0
res = 0
for i in range(L):
    if arr[i] > n:
        if i == 0:
            start = 1
            end = arr[i] - 1
        else:
            start = arr[i-1] + 1
            end = arr[i] - 1
        break
    elif arr[i] == n:
        print(0)
        exit()

print((end - n + 1) * (n+1-start) - 1)

# for i in range(start, n+1):
#     res += end - n + 1



# 34 59, 34 60 ... 34 99 -> 40 -> 99 - 59
# 35 59 -> 35 99 -> 40
# 59 60, 59 61 ... 59, 99 -> 39

