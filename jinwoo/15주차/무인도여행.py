# 45분
# 재귀제한 시발...
import sys
sys.setrecursionlimit(int(1e6))
dy = [-1,0,1,0]
dx = [0,1,0,-1]
v = [[-1]*110 for _ in range(110)]

def dfs(r,c,R,C,maps):
    global cnt
    v[r][c]=1
    print(maps[r][c])
    cnt+=int(maps[r][c])
    for dir in range(4):
        nr = r + dy[dir]
        nc = c + dx[dir]
        if nr<0 or nc<0 or nr>=R or nc>=C:
            continue
        if v[nr][nc] != -1 or maps[nr][nc]=='X':
            continue
        dfs(nr,nc,R,C,maps)
    
def solution(maps):
    global cnt
    ans = []
    R = len(maps)
    C = len(maps[0])
    for i in range(R):
        for j in range(C):
            if v[i][j]==-1 and maps[i][j]!='X':
                cnt=0
                dfs(i,j,R,C,maps) 
                ans.append(cnt)
                print("@@")
                
    if len(ans)==0:
        ans=[-1]
    ans.sort()
    return ans