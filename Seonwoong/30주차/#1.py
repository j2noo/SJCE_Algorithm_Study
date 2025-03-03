N = int(input().strip())            
A = list(map(int, input().split())) 
k = int(input().strip())            

chunk_size = N // k

for start in range(0, N, chunk_size):
    A[start:start+chunk_size] = sorted(A[start:start+chunk_size])

print(*A)