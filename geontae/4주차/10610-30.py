N = int(input())
arr = []

for i in str(N):
    arr.append(int(i))

arr.sort(reverse=True)
result = int(''.join(map(str, arr)))

if result % 30 == 0:
    print(result)
else:
    print(-1)


