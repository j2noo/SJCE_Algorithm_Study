import sys

n, m = map(int, input().split())
cnt_arr = [0] * n
attack_arr = [[0, 0], [0, 0]]

for i in range(n):
    row = list(map(int, input().split()))
    cnt_arr[i] = row.count(1)

for i in range(2):
    attack_arr[i][0], attack_arr[i][1] = map(int, input().split())
    attack_arr[i][0] -= 1
    attack_arr[i][1] -= 1

for i in range(2):
    for s in range(attack_arr[i][0], attack_arr[i][1] + 1):
        if cnt_arr[s] > 0:
            cnt_arr[s] -= 1

ans = sum(cnt_arr)
print(ans)
