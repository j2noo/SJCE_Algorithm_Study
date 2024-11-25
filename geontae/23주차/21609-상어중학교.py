import copy

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = []
rainbow = []
rainbow.append(0)
res = 0


def count(arr, i, j, target):
    cnt = 1
    visited.append([i, j])
    arr[i][j] = -2

    for d in range(4):
        if 0 <= i+dx[d] < n and 0 <= j+dy[d] < n:
            if arr[i+dx[d]][j+dy[d]] == target:
                arr[i + dx[d]][j + dy[d]] = -2
                cnt += count(arr, i+dx[d], j+dy[d], target)
            elif arr[i+dx[d]][j+dy[d]] == 0:
                rainbow[0] += 1
                cnt += count(arr, i + dx[d], j + dy[d], target)
    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


while True:
    max_cnt = 0
    max_list = []
    max_rainbow = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                cnt = count(copy.deepcopy(arr), i, j, arr[i][j])
                if max_cnt < cnt:
                    max_cnt = cnt
                    max_list = copy.deepcopy(visited)
                    max_rainbow = rainbow[0]
                elif max_cnt == cnt and max_rainbow <= rainbow[0]:
                    max_cnt = cnt
                    max_list = copy.deepcopy(visited)
                    max_rainbow = rainbow[0]
                visited = []
                rainbow[0] = 0

    if max_cnt < 2:
        break
    res += max_cnt ** 2
    for i, j in max_list:
        arr[i][j] = -2
    # 중력 작용
    for i in range(n-1):
        for j in range(n):
            if arr[i + 1][j] == -2:
                for k in range(i + 1, 1, -1):
                    if arr[k][j] == -1:
                        break
                    arr[k][j] = arr[k - 1][j]
                arr[0][j] = -2
    tmp = copy.deepcopy(arr)
    # 90도 회전
    for i in range(n):
        for j in range(n):
            arr[j][i] = tmp[i][n-j-1]
    # 중력 작용
    for i in range(n-1):
        for j in range(n):
            if arr[i+1][j] == -2:
                for k in range(i+1, 1, -1):
                    if arr[k][j] == -1:
                        break
                    arr[k][j] = arr[k-1][j]
                arr[0][j] = -2

    # for i in range(n):
    #     for j in range(n):
    #         if arr[i][j] < 0 :
    #             continue
    #         if i+1 < n and arr[i+1][j] == -2:
    #             arr[i+1][j] = arr[i][j]
    #             arr[i][j] = -2
    for i in range(n):
        print(arr[i])
    print("---------------------")
    # 00 04
    # 10 03
    # 20 02
    # 30 01
    # 40 00
    #
    # 10 41
    # 11 31
    # 12 21
    # 13 11
    # 14 01


print(res)
