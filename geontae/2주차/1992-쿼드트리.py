N = int(input())

arr = list(input() for _ in range(N))


def checkAll(i, j, n):
    initial = arr[i][j]
    for l in range(i, i+n):
        for k in range(j, j+n):
            if arr[l][k] != initial:
                return -1
    return initial


def recursive(i, j, n):
    if n == 1:
        return arr[i][j]
    else:
        result = checkAll(i, j, n)
        if result != -1:
            return result
        else:
            n = int(n/2)
            return ("(" +
                    recursive(i, j, n) +
                    recursive(i, j+n, n) +
                    recursive(i+n, j, n) +
                    recursive(i+n, j+n, n) + ")")


print(recursive(0, 0, N))
