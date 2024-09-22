import heapq
# 다익스트라 찾아봣습니다..ㅈㅅ
INF = 987654321

def solution(n, roads, sources, destination):
    # dest에서 출발하는 최단거리
    dist = [INF]*(n+1)
       
    # 인접리스트 만들기
    adj_li = [[] * (n+1) for i in range(n+1)]
    for s,e in roads:
        adj_li[s].append(e)
        adj_li[e].append(s)
    
    # 다익스트라
    def dijk():
        dist[destination] = 0 # 나로 향하는 거리는 0
        pq = []
        heapq.heappush(pq,(dist[destination],destination))
        
        # 최단거리 순으로 거리테이블 갱신
        while(len(pq) > 0):
            cur_dist, cur_node = heapq.heappop(pq)
            
            for i in range(len(adj_li[cur_node])):
                next_node = adj_li[cur_node][i]
                # next_dist = 1
                
                # 거리 갱신 시
                if dist[next_node] > dist[cur_node] + 1: # dist[cur_node] 대신 cur_dist
                    dist[next_node] = min(dist[next_node],dist[cur_node] + 1)
                    heapq.heappush(pq,(dist[next_node],next_node))
                    
    dijk()
    answer = []

    for source in sources:
        if dist[source] > 987654320:
            answer.append(-1)
        else :
            answer.append(dist[source])
            
    return answer

# bfs O(V+E) * n이어서 불가