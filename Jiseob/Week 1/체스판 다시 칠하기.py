N, M = map(int, input().split())

board = []
count = []

for _ in range (N):
    board.append(input())

for i in range (N - 7):
    for j in range (M - 7):
        countBlack = 0
        countWhite = 0

        for x in range (i, i + 8):
            for y in range (j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'B':
                        countBlack += 1
                    if board[x][y] != 'W':
                        countWhite += 1
                else:
                    if board[x][y] != 'W':
                        countBlack += 1
                    if board[x][y] != 'B':
                        countWhite += 1

        count.append(countBlack)
        count.append(countWhite)

print(min(count))
