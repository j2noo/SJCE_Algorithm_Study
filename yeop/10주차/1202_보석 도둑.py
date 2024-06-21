import heapq

# 입력
N, K = map(int, input().split()) # N: 상점 내 보석 개수 K: 가방 개수
jewelry = []
bags = []
for _ in range(N):
  M, V = map(int, input().split()) # M: 무게, V: 가격
  jewelry.append((M, V))
for _ in range(K):
  C = int(input())
  bags.append(C)
  
jewelry.sort(reverse=True)
bags.sort()

# 가방에 자기 무게로 담을 수 있는 가장 비싼 애를 넣자.
cost = 0
queue = [] # 가격 내림차순 담을 수 있는 보석들
for bag in bags:
  while jewelry:
    j_weight, j_value = jewelry.pop()
    if bag < j_weight:
      jewelry.append((j_weight, j_value))
      break
    heapq.heappush(queue, (-j_value, j_weight))
  
  if queue:
    j_value, j_weight = heapq.heappop(queue)
    cost -= j_value

print(cost)