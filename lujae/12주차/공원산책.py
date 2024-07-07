# 풀이에 걸린 시간: 17분 50초
# 풀이에 사용한 접근: 그냥 품
def isRange(y, x, h, w):
    return 0 <= y < h and 0 <= x < w


def isCrushed(park, y, x, nextY, nextX):
    if y == nextY:
        for i in range(min(x, nextX), max(x, nextX) + 1):
            if park[y][i] == 'X':
                return True
        return False
    else:
        for i in range(min(y, nextY), max(y, nextY) + 1):
            if park[i][x] == 'X':
                return True
        return False
def solution(park, routes):
    dirMap = {}
    dirMap["N"] = (-1, 0)
    dirMap["S"] = (1, 0)
    dirMap["W"] = (0, -1)
    dirMap["E"] = (0, 1)

    currentY = 0
    currentX = 0

    H = len(park)
    W = len(park[0])

    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                currentY = i
                currentX = j

    for route in routes:
        dir, distance = route.split(" ")
        distance = int(distance)

        nextY = currentY + dirMap[dir][0] * distance
        nextX = currentX + dirMap[dir][1] * distance

        if isRange(nextY, nextX, H, W) and not isCrushed(park, currentY, currentX, nextY, nextX):
            currentY = nextY
            currentX = nextX

    return [currentY, currentX]