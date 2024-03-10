import sys
sys.setrecursionlimit(10**6)

cache = [[[-1] * 16 for i in range(16)] for j in range(3)]
nextState = [(0, 2), (1, 2), (0, 1, 2)]
delta = [(0, 1), (1, 0), (1, 1)]

def isRange(y,x):
    return 0 <= y < N and 0 <= x < N

def sol(state, y, x):
    if y == N - 1 and x == N - 1:
        return 1
    if cache[state][y][x] != -1:
        return cache[state][y][x]

    ret = 0
    for ns in nextState[state]:
        nextY = y + delta[ns][0]
        nextX = x + delta[ns][1]

        if isRange(nextY, nextX):
            if ns != 2 and arr[nextY][nextX] != 1:
                ret += sol(ns, nextY, nextX)
            if ns == 2 and arr[y + 1][x] != 1 and arr[y][x + 1] != 1 and arr[y + 1][x + 1] != 1:
                ret += sol(ns, nextY, nextX)

    cache[state][y][x] = ret
    return ret

N = int(input())
arr = []

for i in range(N):
    tmpArr = list(map(int, sys.stdin.readline().split(" ")))
    arr.append(tmpArr)

print(sol(0, 0, 1))