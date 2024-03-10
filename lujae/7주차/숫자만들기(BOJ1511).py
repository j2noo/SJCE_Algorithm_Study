def checkCntOver(cntList):
    sumList = [0 for i in range(10)]

    for i in range(10):
        for j in range(j):
            if i != j:
                sumList[i] += cntList[j]

    overNumber = -1
    for i in range(10):
        if cntList[i] - 1 >= sumList[i]:
            overNumber = i

    if cntList[overNumber] > sumList[overNumber]:
        tmpRet = ""
        for i in range(sumList[overNumber]):
            for j in range(9, -1, 0):
                if j != overNumber and cntList[j] > 0:
                    tmpRet += str(overNumber) + str(j)
                    cntList[j] -= 1



cntList = list(map(int, input().split(" ")))

ret = ""
arr = []
for i in range(10):
    if cntList[i] != 0:
        arr.append((i, cntList[i]))
arr.sort(key = lambda x : -x[0])

idx = 0
while len(arr) >= 2:
    (num, cnt) = arr[idx % 2]
    arr.remove((num, cnt))
    ret += str(num)

    if cnt - 1 != 0:
        arr.append((num, cnt - 1))
    else:
        idx = 1

    arr.sort(key = lambda x : -x[0])

    idx += 1

if ret != "" and len(arr) == 1:
    (num, cnt) = arr[0]

    if ret[-1] != str(num):
        ret += str(num)
        cnt -= 1

    for i in range(cnt):
        pos = ret.index(str(num))

        if pos == 0:
            break
        if pos == 1 and num == 0:
            break
        ret = ret[:pos - 1] + str(num) + ret[pos - 1:]

if ret == "":
    print(0)
else:
    print(ret)
