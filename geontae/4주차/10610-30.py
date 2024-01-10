N = int(input())

arr = []
cnt = 0
for i in str(N):
    cnt += int(i)
    arr.append(int(i))

arr.sort(reverse=True)
result = int(''.join(map(str, arr)))

if cnt % 3 == 0 and result % 10 == 0:
    print(result)
else:
    print(-1)


