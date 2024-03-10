n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

cnt = 0
# 이동한 뒤, 유효한 이동인지 확인 (별로임)
def sol(i, j, x):
    global cnt

    if i >= n or j >= n:
        return 0
    elif arr[i][j] == 1:
        return 0
    elif x == 1 and j == n-1:
        return 0
    elif x == 2 and i == n-1:
        return 0
    elif x == 3 and (arr[i-1][j] == 1 or arr[i][j-1] == 1):
        return 0
    # 마지막 지점에서 대각선 이동이 안될 경우(n,n은 0이지만 그 위 아래가 1일 경우)
    # 정상 이동이라 판단해버림 ㅠ
    elif i == j == n - 1:
        cnt += 1
        return 0

    # 파이프가 가로인 경우
    if x == 1:
        # 다음 칸이 벽일 경우

        # 가로로 한칸 이동
        sol(i, j+1, 1)
        # 대각선으로 한칸 이동
        sol(i+1, j+1, 3)
    # 파이프가 세로인 경우
    if x == 2:
        sol(i+1, j, 2)
        sol(i+1, j+1, 3)
    # 파이프가 대각선인 경우
    if x == 3:
        sol(i, j+1, 1)
        sol(i+1, j, 2)
        sol(i+1, j+1, 3)


x = sol(0, 1, 1)
print(cnt)