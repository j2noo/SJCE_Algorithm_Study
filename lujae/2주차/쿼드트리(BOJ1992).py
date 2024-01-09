import sys
sys.setrecursionlimit(10**8)

def allSame(startY, startX, size, num):
    for i in range(size):
        for j in range(size):
            idxY = startY + i
            idxX = startX + j
            if arr[idxY][idxX] != num:
                return False

    return True

def quadTree(startY, startX, size):
    if(size == 1):
        return str(arr[startY][startX])

    if(allSame(startY, startX, size, 0)):
        return "0"
    if(allSame(startY, startX, size, 1)):
        return "1"

    nextSize = size // 2

    firstArea = quadTree(startY, startX, nextSize)
    secondArea = quadTree(startY, startX + nextSize, nextSize)
    thirdArea = quadTree(startY + nextSize, startX, nextSize)
    forthArea = quadTree(startY + nextSize, startX + nextSize, nextSize)

    return "(" + firstArea + secondArea + thirdArea + forthArea + ")"



N = int(input())
arr = [[int(n) for n in input()]for _ in range(N)]

print(quadTree(0, 0, N))