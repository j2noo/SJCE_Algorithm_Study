x, y, z = map(int, input().split())

a = round((x + y - z) / 2, 1)
b = round((x - y + z) / 2, 1)
c = round((-x + y + z) / 2, 1)
if a > 0 and b > 0 and c > 0:
    print(1)
    print(a, b, c)
else:
    print(-1)