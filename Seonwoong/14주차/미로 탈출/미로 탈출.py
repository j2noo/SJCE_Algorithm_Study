from collections import deque

#시작점과 레버 위치 찾기
def find_point(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='S':
                start=(j,i)
            if maps[i][j]=='L':
                lever=(j,i)
    
    return start, lever

#bfs 함수 시작점에서 target까지 최단 경로 찾기, 도달 못하면 -1 반환
def bfs(start, maps, target):
    dx=[1,0,0,-1]
    dy=[0,1,-1,0]
    x, y= start
    queue=deque([(x,y,0)])
    visited=[[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[y][x]=True
    
    while queue:
        x,y,d=queue.popleft()
        if maps[y][x]==target: 
            return d
    
        for i in range(4):
            X,Y=x+dx[i], y+dy[i]
            if 0<=X<len(maps[0]) and 0<=Y<len(maps) and not visited[Y][X] and maps[Y][X]!='X':
                visited[Y][X]=True
                queue.append((X,Y,d+1))       
    return -1
    
def solution(maps):
    start, lever= find_point(maps)
    #start에서 lever, lever에서 End까지 경로 탐색
    
    #둘중에 하나라도 도달 못하면 -1반환
    LD=bfs(start, maps, 'L')
    if LD==-1: return -1
    ED=bfs(lever, maps,'E')
    if ED==-1: return -1
    
    #최단경로길이 반환
    return LD+ED
