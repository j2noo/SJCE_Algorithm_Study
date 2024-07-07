n = 6
k = 4
enemy = [3, 3, 3, 3]

## 실패지점 찾기

def determine(tmpEnemy):
    tmpEnemy.sort(reverse=True)
    tmpSum = sum(tmpEnemy[k:])
    return tmpSum <= n

def binarySearch(start, end):
    if start >= end:
        return start

    mid = (start + end) // 2

    if determine(enemy[:mid + 1]):
        return binarySearch(mid + 1, end)
    else:
        return binarySearch(start, mid)

idx = binarySearch(0, len(enemy))
print(idx)
# print(min(len(enemy), idx))