
def getDirSame(state, y, x, dir):
    ret = 0
    color = state[y][x]

    for i in range(1, 21):
        deltaY = i * dir[0]
        deltaX = i * dir[1]

        if state[y + deltaY][x + deltaX] != color:
            return ret

        ret += 1

    return 0

def isFinish(state, y, x):
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    dx = [1, 1, 0, -1, -1, -1, 0, 1]

    # 가로
    r = getDirSame(state, y, x, (dy[0], dx[0]))
    l = getDirSame(state, y, x, (dy[4], dx[4]))
    if r + l == 4: return True

    # 세로
    u = getDirSame(state, y, x, (dy[2], dx[2]))
    d = getDirSame(state, y, x, (dy[6], dx[6]))
    if u + d == 4: return True

    # 우상향 대각
    ru = getDirSame(state, y, x, (dy[1], dx[1]))
    ld = getDirSame(state, y, x, (dy[5], dx[5]))
    if ru + ld == 4: return True

    # 우하향 대각
    rd = getDirSame(state, y, x, (dy[7], dx[7]))
    lu = getDirSame(state, y, x, (dy[3], dx[3]))
    if rd + lu == 4: return True

    return False

def sol(arr):
    state = [[0] * 22 for i in range(22)]

    for i in range(len(arr)):
        y, x = arr[i]
        color = 1 if i % 2 == 0 else -1
        state[y][x] = color

        if isFinish(state, y, x):
            return i + 1

    return -1

N = int(input())
arr = []
for i in range(N):
    (y, x) = map(int, input().split(" "))
    arr.append((y, x))

print(sol(arr))