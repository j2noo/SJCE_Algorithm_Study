N = int(input())

lost_li = list(map(int, input().split()))
get_li = list(map(int, input().split()))

dp = [[-1] * 101 for _ in range(101)]  # 0??

dp[0][100] = 0  # 첫번째 안함
if lost_li[0] < 100:
    dp[0][100 - lost_li[0]] = get_li[0]  # 첫번째 함

for i in range(N):
    if i == 0: continue

    lost = lost_li[i]
    get = get_li[i]

    # 남은체력  
    for hp in range(101):
        # 안함
        dp[i][hp] = max(dp[i][hp], dp[i - 1][hp])

        # 함
        if hp - lost <= 0:
            continue
        dp[i][hp - lost] = max(dp[i][hp - lost], dp[i - 1][hp] + get)

ans = max(dp[N - 1])
print(ans)

# dp[idx][hp] : idx번까지 진행되고, 남은체력이 hp일때 최대 기쁨
