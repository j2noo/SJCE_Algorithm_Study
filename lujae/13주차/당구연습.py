import math


def calDistanceWithUp(m, n, startX, startY, objX, objY):
    diffHeight1 = n - startY
    diffHeight2 = n - objY

    s = abs(objX - startX) / (1 + diffHeight2 / diffHeight1)
    kPow2 = s ** 2 + diffHeight1 ** 2

    return kPow2 * ((1 + diffHeight2 / diffHeight1) ** 2)

def calDistanceWithAngle1(m, n, startX, startY, objX, objY):
    d1 = math.sqrt((m - objX) ** 2 + (n - objY) ** 2) + math.sqrt((m - startX) ** 2 + (n - startY) ** 2)
    d2 = math.sqrt((objX) ** 2 + (objY) ** 2) + math.sqrt((startX) ** 2 + (startY) ** 2)

    return min(d1, d2)
def calDistanceWithAngle1(m, n, startX, startY, objX, objY):
    d1 = math.sqrt((m - objX) ** 2 + (n - objY) ** 2) + math.sqrt((m - startX) ** 2 + (n - startY) ** 2)
    d2 = math.sqrt((objX) ** 2 + (objY) ** 2) + math.sqrt((startX) ** 2 + (startY) ** 2)

    return min(d1, d2)


def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        ret = 987654321
        objX, objY = ball

        ret = min(ret, calDistanceWithUp(m, n, startX, startY, objX, objY))
        ret = min(ret, calDistanceWithUp(n, m, n - startY, startX, n - objY, objX))
        ret = min(ret, calDistanceWithUp(m, n, m - startX, n - startY, m - objX, n - objY))
        ret = min(ret, calDistanceWithUp(n, m, startY, m - startX, objY, m - objX))

        if n / m == startY / startX and n / m == objY / objX:
            ret = min(ret, calDistanceWithAngle1(m, n, startX, startY, objX, objY))
        if n / m == n - startY / startX and n / m == n - objY / objX:
            ret = min(ret, calDistanceWithAngle2(m, n, startX, startY, objX, objY))

    return answer