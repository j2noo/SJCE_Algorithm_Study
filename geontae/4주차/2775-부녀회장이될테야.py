T = int(input())

result = []
houses = []

# 재귀가 안되고 중복 없으면 반복문으로 풀어보기

for _ in range(T):
    k = int(input())
    n = int(input())
    houses = [[1]*(n+1) for _ in range(k+1)]
    for i in range(1, n+1):
        houses[0][i] = i
    for num in range(2, n+1):
        for floar in range(1, k+1):
            houses[floar][num] = houses[floar-1][num] + houses[floar][num-1]
    result.append(houses[k][n])

for r in result:
    print(r)
