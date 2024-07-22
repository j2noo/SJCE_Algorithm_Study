# 시간 19분
# BFS 2번

import collections
def isRange(y, x, n, m):
    return 0 <= y < n and 0 <= x < m
def getMinTravelTime(maps, startPos, endPos):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    sY, sX = startPos
    eY, eX = endPos

    height = len(maps)
    width = len(maps[0])

    discovered = [[False] * width for i in range(height)]

    deque = collections.deque()
    deque.append((sY, sX, 0))
    discovered[sY][sX] = True

    while deque:
        hY, hX, hT = deque.popleft()

        if hY == eY and hX == eX:
            return hT

        for i in range(4):
            tY = hY + dy[i]
            tX = hX + dx[i]

            if isRange(tY, tX, height, width) and not discovered[tY][tX] and maps[tY][tX] != 'X':
                discovered[tY][tX] = True
                deque.append((tY, tX, hT + 1))

    return -1

def solution(maps):
    startPos = leverPos = endPos = (-1, -1)

    height = len(maps)
    width = len(maps[0])

    for i in range(height):
        for j in range(width):
            if maps[i][j] == 'S':
                startPos = (i, j)
            elif maps[i][j] == 'L':
                leverPos = (i, j)
            elif maps[i][j] == 'E':
                endPos = (i, j)

    t1 = getMinTravelTime(maps, startPos, leverPos)
    t2 = getMinTravelTime(maps, leverPos, endPos)

    if t1 == -1 or t2 == -1:
        return -1

    return t1 + t2