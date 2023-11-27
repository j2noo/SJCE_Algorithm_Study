N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

A.sort()

for i in range (N):
    S += A[i] * max(B)
    B.remove(max(B))

print(S)