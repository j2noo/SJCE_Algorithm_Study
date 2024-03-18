import sys

N, M = map(int, sys.stdin.readline().split(" "))

arr = [i for i in range(0, N + 1)]

for i in range (0, M):
    s, e = map(int, sys.stdin.readline().split(" "))

    slicedArr = arr[s: e + 1]
    arr = [0] + arr[1:s] + slicedArr[::-1] + arr[e + 1:]

ret = ""
for i in range(1, N + 1):
    ret += str(arr[i]) + " "
print(ret)