#시간: 19분

import collections

def getStartPosition(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                return (i, j)

    return (-1, -1)

def isRange(y, x, n, m):
    return 0 <= y < n and 0 <= x < m
def calcutateNextPos(board, posY, posX, dirIdx):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    hereY = posY
    hereX = posX

    while True:
        thereY = hereY + dy[dirIdx]
        thereX = hereX + dx[dirIdx]

        if isRange(thereY, thereX, len(board), len(board[0])) and board[thereY][thereX] != 'D':
            hereY = thereY
            hereX = thereX
        else:
            break

    return (hereY, hereX)

def solution(board):
    discovered = [[False for j in range(len(board[i]))] for i in range(len(board))]
    deque = collections.deque()
    posY, posX = getStartPosition(board)
    deque.append((posY, posX, 0))
    discovered[posY][posX] = True

    while deque:
        hereY, hereX, cnt = deque.popleft()

        if board[hereY][hereX] == 'G':
            return cnt

        for i in range(4):
            nextY, nextX = calcutateNextPos(board, hereY, hereX, i)

            if not discovered[nextY][nextX]:
                deque.append((nextY, nextX, cnt + 1))
                discovered[nextY][nextX] = True

    return -1