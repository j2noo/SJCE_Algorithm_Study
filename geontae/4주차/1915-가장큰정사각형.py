n, m = map(int, input().split())

array = [list(map(int, input())) for _ in range(n)]
max = 1
f = 0

for i in range(0,n):
    for j in range(0,m):
        if array[i][j] != 0:
            f = 1
            if i != 0 and j != 0:
                if array[i-1][j] != 0 and array[i][j-1] != 0 and array[i-1][j-1] != 0:
                    if array[i-1][j] == array[i][j-1] == array[i-1][j-1]:
                        array[i][j] += array[i-1][j]
                    else:
                        array[i][j] += min(array[i-1][j], array[i][j-1], array[i-1][j-1])
                    if array[i][j] > max:
                        max = array[i][j]

if f == 1:
    print(max**2)
else:
    print(0)
