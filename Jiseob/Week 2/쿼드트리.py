N = int(input())
video = []

for _ in range (N):
    video.append(list(map(int, input())))

def quadTree(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if video[x][y] != video[i][j]:
                print("(", end="")

                # 4사분면으로 나눈다.
                quadTree(x, y, n // 2) # 1사분면
                quadTree(x, y + n // 2, n // 2) # 2사분면
                quadTree(x + n // 2, y, n // 2) # 3사분면
                quadTree(x + n // 2, y + n // 2, n // 2) # 4사분면

                print(")", end="")
                return
    
    if video[x][y] == 1:
        print(1, end="")
    else:
        print(0, end="")

quadTree(0, 0, N)