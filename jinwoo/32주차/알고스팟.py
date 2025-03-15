# dfs? with 방문지도
import sys
sys.setrecursionlimit(10**5)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
ans = 987654321

def dfs(r, c):
    global isVisited
    global lands
    
    lands.append((r,c))

    for dir in range(4):
        nr = r + dy[dir]
        nc = c + dx[dir]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if isVisited[nr][nc] == 1:
            continue
            
        if arr[nr][nc] == '0':
            isVisited[nr][nc] = 1
            dfs(nr, nc)

     


M, N = map(int, input().split())
isVisited = [[0] * M for _ in range(N)]

arr = []
for _ in range(N):
    arr.append(list(input()))
    
lands = []
depth = 0
ans = 0
while True:
    isVisited = [[0] * M for _ in range(N)]
    dfs(0,0)
    for r,c in lands:
        if r == N-1 and c == M-1 :
            print(depth)
            exit()
        for dir in range(4):
            nr = r + dy[dir]
            nc = c + dx[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if isVisited[nr][nc] == 1:
                continue
            if arr[nr][nc] == 0 : 
                continue
            arr[nr][nc] = '0'
            isVisited[nr][nc] = 1
            
    depth+=1
    lands.clear()
    
