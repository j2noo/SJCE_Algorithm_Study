n, m = map(int, input().split())
card = list(map(int, input().split()))
res = 0
for _ in range(m):
    card.sort()
    new_value = card[0] + card[1]
    card[0] = new_value
    card[1] = new_value

for i in range(n):
    res += card[i]

print(res)
