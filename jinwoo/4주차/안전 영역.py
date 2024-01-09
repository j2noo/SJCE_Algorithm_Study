import sys
sys.setrecursionlimit(10**5)


# r,c에서 dfs
def dfs(r,c,height):
    global visited
    
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    
    visited[r][c]=1
    for dir in range(4):
        nr = r+dy[dir]
        nc = c+dx[dir]
        if  0 <= nr < N and  0 <= nc < N and visited[nr][nc]==0 and arr[nr][nc] > height:
            dfs(nr,nc,height)

#높이 height의 비가 내릴 때 안전영역의 개수
def calc(height):
    global visited
    cnt=0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 물에 잠기지 않는 영역 탐색
            if visited[i][j]==0 and arr[i][j]>height:
                cnt+=1
                dfs(i,j,height)
    # print("calc : ",height,cnt)
    return cnt

N=int(input())

arr=[list(map(int,input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
ans=1

for height in range(1,102):
    ans=max(ans,calc(height))
    
print(ans)
    
