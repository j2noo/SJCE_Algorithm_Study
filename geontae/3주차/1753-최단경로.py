import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())

graph = {}
distance = [INF] * (V + 1)
# visited = [False] * (V + 1)
heap = []

for i in range(0, V+1):
    graph[i] = []


def dijkstra(start):
    # 시작 노드의 거리를 0으로 설정
    # 파이썬 힙큐는 첫번째 원소를 기준으로 우선순위 큐를 구성
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    # 시작 노드를 방문 처리
    # visited[start] = True

    # 시작 노드와 연결된 노드의 거리를 설정
    # !! 어차피 힙에서 시작 노드가 빠지므로 중복되는 부분임
    # for node, weight in graph[start]:
    #     heapq.heappush(heap, (weight, node))
    #     distance[node] = weight

    while heap:
        weight, now = heapq.heappop(heap)
        # visited[now] = True

        # !! 빼도 상관없을 것 같고 이해도 안가서 빼보니 됨
        # if distance[now] < weight:
        #     continue
        if now == 0:
            break
        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[now] + j[1]
                heapq.heappush(heap, (distance[j[0]], j[0]))


for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
