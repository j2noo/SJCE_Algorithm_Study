import sys

input = sys.stdin.readline

# N: 바구니 개수
# M: 바구니 역순으로 변경할 횟수
N, M = list(map(int, input().split()))
basket = [_ for _ in range(1, N + 1)]

#sol
for _ in range(M):
  i, j = list(map(int, input().split()))
  section = basket[i-1:j]
  basket[i-1:j] = section[::-1]
  
print(' '.join(str(c) for c in basket))