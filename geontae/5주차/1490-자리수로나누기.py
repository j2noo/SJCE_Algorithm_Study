n = int(input())

arr = list(map(int, str(n)))
res = arr.copy()
start = len(arr)
last = len(arr)
f=0
for x in arr:
    if x!=0 and n % x != 0:
        f = 1
if f == 0:
    print(n)
else:
    res.append(0)
    while True:
        if res[last] == 10:
            i = 1
            res[last] = 0
            if last == start:
                res[last] = 0
                res.append(0)
                last += 1
            # 윗 자리수를 1 증가시킴
            else:
                while True:
                    res[last-i] += 1
                    if res[last-i] == 10:
                        if last - i == start:
                            res.append(0)
                            for j in range(start, last):
                                res[j] = 0
                            last += 1
                            break
                        res[last-i] = 0
                        i += 1
                    else:
                         break
        num = int(''.join(map(str, res)))

        f = 0
        for x in arr:
            if x!=0 and num % x != 0:
                f = 1
        if f == 0:
            print(num)
            break
        else:
            res[last] += 1
            #print(res)