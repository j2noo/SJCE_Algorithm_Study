import sys
sys.setrecursionlimit(10**5)

dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 가장자리부터 공기인 곳 탐색 
def dfs(r,c):
    visited[r][c]=1
    for dir in range(4):
        nr = r+dy[dir]
        nc = c+dx[dir]
        
        if nr<0 or nc <0 or nr>=R or nc>=C :
            continue
        
        # 공기와 접촉한 치즈는 녹기
        if visited[nr][nc]==-1 and arr[nr][nc] == 1 :
            melted.append([nr,nc])
            visited[nr][nc]=1
            
        if visited[nr][nc]==-1 and arr[nr][nc]== 0:
            dfs(nr,nc)
            
            
cntCheese=0
R, C = map(int,input().split())
arr = []

for _ in range(R):
    arr.append(list(map(int,input().split())))
    
# 가장자리 dfs
edges = []
for i in range(R):
    for j in range(C):
        if i==0 or j==0 or i==R-1 or j==C-1:
            edges.append([i,j])
        if arr[i][j]==1:
            cntCheese+=1
            
depth = 0
prev = cntCheese

while(cntCheese>0):
    depth+=1
    visited = [[-1]*C for _ in range(R)]
    melted = []
    for r,c in edges :
        if visited[r][c] == -1:
            dfs(r,c)   
        
    # 남은 치즈 저장
    prev = cntCheese 
            
    # arr 업데이트
    for r,c in melted:
        arr[r][c]=0
    
    # 남은 치즈 업데이트
    cntCheese = cntCheese - len(melted)
    
print(depth)
print(prev)