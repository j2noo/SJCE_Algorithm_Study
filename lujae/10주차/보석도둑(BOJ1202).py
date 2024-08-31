import heapq

N, K = map(int, input().split(" "))

ret = 0
arrMV = []
heapVM = []
arrC = []

for i in range(N):
    M, V = map(int, input().split(" "))
    arrMV.append((M, V))

for i in range(K):
    c = int(input())
    arrC.append(c)

arrMV.sort(key=lambda x: x[0])
arrC.sort()
cnt = 0
idx = 0

for i in range(K):
    while idx < N and arrMV[idx][0] <= arrC[i]:
        M = arrMV[idx][0]
        V = arrMV[idx][1]

        heapq.heappush(heapVM, (-V, M))
        idx += 1

    if heapVM:
        (V, M) = heapq.heappop(heapVM)
        ret += -V

print(ret)