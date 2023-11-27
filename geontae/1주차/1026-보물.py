n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list()
D = A.copy()
D.sort()
for j in range(0, n):
    max = 0
    for i in range(0, n):
        if i not in C:
            if B[i] >= max:
                max = B[i]
                maxIndex = i
    A[maxIndex] = D[j]

    C.append(maxIndex)

cnt = 0
for k in range(0, n):
    cnt += A[k] * B[k]
# print(A, B)
print(cnt)
