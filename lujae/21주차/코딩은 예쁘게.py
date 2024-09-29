# 구현
# 파이썬 split(" ")했더니, valueError,,
def get_idx_not_0(li):
    for i in range(len(li)):
        if li[i] != 0:
            return i

    return len(li)


N = int(input())
ret = 0

arr = []
rest = []
for i in range(2):
    arr.append(list(map(int, input().split())))

for i in range(N):
    rest.append(arr[1][i] - arr[0][i])

while True:
    start = get_idx_not_0(rest)
    if start == len(rest):
        break
    end = start + 1
    delta = 0

    if rest[start] > 0:
        while end < len(rest):
            if rest[end] <= 0:
                break
            end += 1
        delta = min(rest[start:end])
    elif rest[start] < 0:
        while end < len(rest):
            if rest[end] >= 0:
                break
            end += 1

        delta = max(rest[start:end])

    for i in range(start, end):
        rest[i] -= delta
    ret += abs(delta)

print(ret)
