# 키가 제일 작은사람부터, 찾기
# 왼쪽에 0명 -> 본인은 0
# 왼쪽에 1명 -> 본인은 1

## 키가 2인사람
# 왼쪽에 0명 -> 키가1인사람이 있으면 1, 없으면 0
# 왼쪽에 n명 -> 키가 1인시람이 있으면 n+1, 없으면 n

## 키가 3
# 왼쪽에 n명 -> 키 1,2 있으면 ~~

N = int(input())
li = list(map(int, input().split()))
ans = [-1] * N

for idx, val in enumerate(li):
    # ans[val] = idx
    # val칸 실이동함
    pos = 0
    while ans[pos] != -1:
        pos += 1

    for i in range(val):
        if ans[pos] == -1:
            pos += 1
            while ans[pos] != -1:
                pos += 1

    # val == 0 인경우도 체크

    ans[pos] = idx + 1
print(*ans)