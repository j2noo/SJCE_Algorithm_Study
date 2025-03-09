# bfs?
from collections import deque
# 30분

dy = [-1,0,1,0]
dx = [0,1,0,-1]

R,C,T = map(int,input().split())
arr = []
for _ in range(R):
    arr.append(list(input()))

sr,sc = -1,-1
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'G':
            sr,sc = i,j

isVisited = [[0]*C for _ in range(R)]
ans = 0

def dfs(r,c,move,goguma):
    global ans

    ans = max(ans,goguma)
    if move == T :
        return 

    for dir in range(4):
        nr = r + dy[dir]
        nc = c + dx[dir]
        
        if nr<0 or nc<0 or nr >=R or nc>=C :
            continue
        if isVisited[nr][nc] == 1 or arr[nr][nc] == '#':
            continue
        if arr[nr][nc] == 'S' :
            arr[nr][nc] = '.'
            dfs(nr,nc,move+1,goguma+1)
            arr[nr][nc] = 'S'
        else :
            dfs(nr, nc, move + 1, goguma)

# isVisited[sr][sc] = 1
dfs(sr,sc,0,0)

print(ans)