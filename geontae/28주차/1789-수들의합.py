n = int(input())
cnt = 0
i = 0
while True:
    i += 1
    cnt += i
    if cnt > n:
        print(i-1)
        break
    elif cnt == n:
        print(i)
        break
