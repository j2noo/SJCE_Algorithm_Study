# time, parents[] -> 자식에 추가ㅠ
# dp[n] = n번 건물을 짓는데 드는 최소비용 _. 재귀
INF = float("inf")
N = int(input())

dp = [-1] * (N + 1)
costs = [-1] * (N + 1)
in_edges = [[] for _ in range(N + 1)]  # 간선

out_edges = [[] for _ in range(N + 1)]  # 나가는 간선


# v건물을 짓는데 걸리는 시간

def dfs(v):
    if dp[v] != -1:
        return dp[v]  # 이미 계산

    ret = -1
    for inv in in_edges[v]:
        ret = max(ret, dfs(inv) + costs[v])
    dp[v] = ret
    return ret


for idx in range(N):
    idx += 1
    input_li = list(map(int, input().split()))
    costs[idx] = input_li[0]  # 비용
    for j in range(1, len(input_li)):
        if j == len(input_li) - 1:  # -1
            break
        pr = input_li[j]  # 부모
        out_edges[pr].append(idx)
        in_edges[idx].append(pr)  # 나한테 들어오는간선

# print(in_edges) # in_edges.len == 0 이면 루트

root = -1
for v in range(1, N + 1):
    if len(in_edges[v]) == 0:
        dp[v] = costs[v]

# print(out_edges,root)

# 탐색
# dp[root] = costs[root]
for v in range(1, N + 1):
    rett = dfs(v)
    # print(f'{v}건물 : {rett}')
    print(rett)



