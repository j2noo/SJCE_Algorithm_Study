def sol(idx):
    if idx == N:
        return 1

    if(cache[idx] != -1):
        return cache[idx]

    ret = 1;
    for next in range(idx + 1, N + 1):
        if(arr[idx] < arr[next]):
            ret = max(ret, 1 + sol(next))

    cache[idx] = ret
    return ret

N = int(input())
cache = [-1] * (N + 1);
arr = [0] + list(map(int, input().split(" ")))
print(sol(0) - 1)