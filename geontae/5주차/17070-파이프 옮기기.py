n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

cnt = 0


def sol(i, j, x):
    global cnt
    if i == j == n-1:
        cnt += 1
        return 0
    if x == 1:
        if j < n-1 and arr[i][j+1] != 1:
            # 가로로 한칸 이동
            sol(i, j+1, 1)
        if i < n-1 and j < n-1 and arr[i][j+1] != 1 and arr[i+1][j] != 1 and arr[i+1][j+1] != 1:
            # 대각선으로 한칸 이동
            sol(i+1, j+1, 3)
    # 파이프가 세로인 경우
    if x == 2:
        if i < n-1 and arr[i+1][j] != 1:
            sol(i+1, j, 2)
        if i < n - 1 and j < n - 1 and arr[i][j + 1] != 1 and arr[i + 1][j] != 1 and arr[i+1][j+1] != 1:
            sol(i+1, j+1, 3)
    # 파이프가 대각선인 경우
    if x == 3:
        if j < n-1 and arr[i][j+1] != 1:
            sol(i, j+1, 1)
        if i < n-1 and arr[i+1][j] != 1:
            sol(i+1, j, 2)
        if i < n - 1 and j < n - 1 and arr[i][j + 1] != 1 and arr[i + 1][j] != 1 and arr[i+1][j+1] != 1:
            sol(i+1, j+1, 3)
    return 0


if arr[n-1][n-1] != 1:
    sol(0, 1, 1)
print(cnt)
