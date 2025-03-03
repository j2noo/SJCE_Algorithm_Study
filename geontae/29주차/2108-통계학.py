import sys
n = int(input())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
cnt = {}
arr.sort()
max_value = 0
max_arr = []
print(round(sum(arr)/n))
print(arr[n//2])
for x in arr:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 0
    if cnt[x] > max_value:
        max_value = cnt[x]
        max_arr = [x]
    elif cnt[x] == max_value:
        max_arr.append(x)
max_arr.sort(reverse=True)
print(max_arr[len(max_arr) - 2])
print(max(arr) - min(arr))