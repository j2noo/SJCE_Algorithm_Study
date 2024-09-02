# 시간: 51분
# O와 X의 개수
# 승리 판단 유무

def determinWin(board, targetSymbol):
    # 가로 라인 한 줄
    for i in range(3):
        targetSymbolCnt = 0
        for j in range(3):
            if board[i][j] == targetSymbol:
                targetSymbolCnt += 1
        if targetSymbolCnt == 3:
            return True

    # 세로 라인 한 줄
    for i in range(3):
        targetSymbolCnt = 0
        for j in range(3):
            if board[j][i] == targetSymbol:
                targetSymbolCnt += 1
        if targetSymbolCnt == 3:
            return True

    #우하향 대각라인
    targetSymbolCnt = 0
    for i in range(3):
        if board[i][i] == targetSymbol:
            targetSymbolCnt += 1
    if targetSymbolCnt == 3:
        return True

    #우상향 대각라인
    targetSymbolCnt = 0
    for i in range(2, -1, -1):
        if board[i][2 - i] == targetSymbol:
            targetSymbolCnt += 1
    if targetSymbolCnt == 3:
        return True

    return False

def solution(board):
    cntO = cntX = 0

    for line in board:
        for symbol in line:
            if symbol == 'O': cntO += 1
            elif symbol == 'X': cntX += 1

    if not (0 <= cntO - cntX <= 1):
        return 0
    if cntO - cntX == 1 and determinWin(board, targetSymbol='X'):
        return 0
    if cntO - cntX == 0 and determinWin(board, targetSymbol='O'):
        return 0
    if determinWin(board, 'O') and determinWin(board, 'X'):
        return 0

    return 1

print(solution(["X.X", ".OO", "..."]))