import heapq

n,m = map(int,input().split())
heap = list(map(int,input().split()))

heapq.heapify(heap)

for _ in range(m):
    card1 = heapq.heappop(heap)
    card2 = heapq.heappop(heap)

    heapq.heappush(heap,card1+card2)
    heapq.heappush(heap,card1+card2)

print(sum(heap))
