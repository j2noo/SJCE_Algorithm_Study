def sol(arr):
    cntArr = [0] * 10
    for num in arr:
        cntArr[num] += 1

    if sum(arr) % 3 != 0 or cntArr[0] == 0:
        return "-1"

    ret = ""
    for num in range(9, -1, -1):
        tmpStr = str(num) * cntArr[num]
        ret += tmpStr

    return ret

arr = list(map(int, input()))
print(sol(arr))