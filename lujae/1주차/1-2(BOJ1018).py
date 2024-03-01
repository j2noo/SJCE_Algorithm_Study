import sys

def check(board, posY, posX):
    color = ['B', 'W'];
    ret = 65;

    for _ in range(2):
        idx = _;
        cnt = 0

        for i in range(8):
            idx += 1

            for j in range(8):
                if(board[posY + i][posX + j] != color[idx % 2]):
                    cnt += 1

                idx += 1

        ret = min(ret, cnt)

    return ret;

def sol(board, N, M):
    ret = 65;

    for i in range(N - 7):
        for j in range(M - 7):
            ret = min(ret, check(board, i, j))

    return ret

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline() for _ in range(N)]

print(sol(board, N, M))