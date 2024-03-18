import math
import sys

sys.setrecursionlimit(10**6)

def search(addStr, maxSize):
    if len(addStr) == maxSize:
        if int(N + addStr) % MOD == 0:
            return int(N + addStr)
        else:
            return 0

    for i in range(0, 10):
        ret = search(addStr + str(i), maxSize)
        if not ret == 0:
            return ret

    return 0
def sol():
    if int(N) % MOD == 0:
        return N

    for i in range(1, 100000000000):
        ret = search("", i)
        if not ret == 0:
            return ret

N = input()
numSet = set(list(map(int, N)))
MOD = 1

for num in numSet:
    if not num == 0:
        MOD = math.lcm(MOD, num)

print(sol())