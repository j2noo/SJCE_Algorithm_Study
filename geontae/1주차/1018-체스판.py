n, m = map(int, input().split())

arr = list(input() for _ in range(n))

min = 2500
cnt = 0

i = 0
j = 0

startData = ['B', 'W']


for _ in range(n-7):
    for _ in range(m-7):

        # print(i, j)
        for ii in range(0, 2):
            k = j
            l = i
            start = startData[ii]
            # print(start)
            # print(i, j)
            for _ in range(8):
                # print(l, k)
                if j % 2 == 0:
                    for _ in range(8):
                        if k % 2 == 0:
                            if (arr[l][k] != start):
                                cnt += 1
                        else:
                            if (arr[l][k] == start):
                                cnt += 1
                        k += 1
                else:
                    for _ in range(8):
                        if k % 2 == 0:
                            if (arr[l][k] == start):
                                cnt += 1
                        else:
                            if (arr[l][k] != start):
                                cnt += 1
                        k += 1
                l += 1
                k = j
                if start == 'B':
                    start = 'W'
                else:
                    start = "B"
            if (cnt < min):
                min = cnt
            cnt = 0
        j += 1
    i += 1
    j = 0

print(min)
