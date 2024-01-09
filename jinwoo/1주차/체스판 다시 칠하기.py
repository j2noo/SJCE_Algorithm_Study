N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

print(arr)
minCount = float("inf")


for i in range(N - 7):
    for j in range(M - 7):
        for evenColor in ["W", "B"]:
            cnt = 0
            for ii in range(8):
                for jj in range(8):
                    r = i + ii
                    c = j + jj
                    # 짝수칸
                    if (r + c) % 2 == 0:
                        cnt += arr[r][c] == evenColor
                    # 홀수칸
                    else:
                        cnt += arr[r][c] != evenColor
            if minCount > cnt:
                minCount = cnt

print(minCount)
