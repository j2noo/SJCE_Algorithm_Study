N, K = map(int, input().split())

li = [[0] * 2 for _ in range(N+1)]
for i in range(1, N+1):
    w, v = map(int, input().split())
    li[i][0] = w
    li[i][1] = v

# dp[i][j] = 배낭의 최대 무게가 i이고 j번째 아이템까지 확인했을 때의 최대 가치
dp = [[0] * (N+1) for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(1, N+1):
        w = li[j][0]
        v = li[j][1]
        # 물건의 무게가 배낭의 최대 무게보다 적을 시
        if w <= i:
            # 물건의 무게만큼 배낭에서 뺴고 해당 물건을 집어넣은 가치
            new_value = dp[i-w][j-1] + v
            # 물건을 담지않고 지나갈 때 vs 물건을 담을 때
            if dp[i][j-1] < new_value:
                dp[i][j] = new_value
            else:
                # 물건을 담지 않고 지나가므로 전 상태 그대로 현 상태 업데이트
                dp[i][j] = dp[i][j-1]
        # 물건의 무게가 배낭의 최대 무게보다 클 시
        else:
            # 물건을 담지 않고 지나가므로 전 상태 그대로 현 상태 업데이트
            dp[i][j] = dp[i][j - 1]

print(max(max(dp)))
