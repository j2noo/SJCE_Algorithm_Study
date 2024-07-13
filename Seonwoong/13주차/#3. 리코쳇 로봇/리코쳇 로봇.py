from collections import deque

def solution(board):
    n,m=len(board), len(board[0])
    queue=deque()
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    visited=[[0 for _ in range(m)] for _ in range(n)]
    answer=0

    #시작점 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                queue.append([i,j,0])
                
    while queue:
        x, y, answer= queue.popleft()
        #방향 탐색
        for dx, dy in directions:
            mx,my=x+dx,y+dy
            #해당방향으로 이동가능한 위치 찾기
            while 0<=mx<n and 0<=my<m and board[mx][my] !='D':
                mx,my = mx+dx,my+dy
            mx,my=mx-dx,my-dy

            #목표지점에 도달하면 이동횟수 반환
            if board[mx][my]=='G':
                return answer+1
            #이전에 도달한적 없으면 방문 표시 후 덱 추가
            if not visited[mx][my]:
                visited[mx][my]=1
                queue.append([mx,my,answer+1])
    
    #목표지점 도달 X는 -1 반환           
    return -1

# 1시간 11분
# 오랜만에 그래프 탐색 풀었더니 x,y 좌표를 반대로 써서 오래걸렸음, bfs, dfs 문제 더 많이 풀어보자
# 시간복잡도는 O(N^2)
