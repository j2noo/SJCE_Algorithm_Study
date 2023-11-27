import sys
def sol(arr, N):
    A = sorted(arr[0][:])
    B = arr[1][:]

    ret = 0
    for i in range(N):
        bMax = max(B)
        ret += A[i] * bMax
        B.remove(bMax)

    return ret;

N = int(input())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

print(sol(arr, N))
