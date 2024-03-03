from collections import deque

dy=[-1,0,1,0]
dx=[0,1,0,-1]

# r,c 부터 시작하여 높이가 height인 칸을 탐색하기, 모서리를 만나면 안됨
def bfs(r,c,height):
    global ans
    visited = [[0]*C for _ in range(R)]
    queue = deque()
    avail = [] # 물을 채울 수 있는 칸 저장
    
    queue.append([r,c])
    avail.append([r,c])
    visited[r][c]=1
    
    while(len(queue)>0):
        for i in range(len(queue)):
            deq = queue.popleft()
            r=deq[0]
            c=deq[1]
            
            for dir in range(4):
                nr = r+dy[dir]
                nc = c+dx[dir]
                
                #높이가 나보다 낮으면 -1
                if arr[nr][nc] < height:
                    return -1
                
                #높이가 height인 칸만 탐색
                if arr[nr][nc] >height:
                    continue
                
                # 모서리와 맞닿음 -> 실패
                if nr ==0 or nc==0 or nr==R-1 or nc==C-1:
                    return -1
                
                if visited[nr][nc]==0:
                    queue.append([nr,nc])
                    avail.append([nr,nc])
                    visited[nr][nc]=1 #ahah
    
    # 모서리와 맞닿지 않아서 물을 줄 수 있음!
    for r,c in avail:
        # print('height : ',height, 'r,c',r,c)
        arr[r][c]+=1
        ans+=1

T=int(input())
for t in range(T):
    R,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(R)]
    ans=0
    
    # 높이가 height인 칸에 물 1만큼 준다.
    for height in range(1,1001):
        # 테두리가 아니면서 높이가 height인 칸
        for i in range(R):
            for j in range(C):
                if 0 < i < R-1 and 0 < j < C-1 and arr[i][j]==height:
                    #dfs로 물을 채우되, 테두리가 나오면 안됨
                    bfs(i,j,height)
    print(f'Case #{t+1}: {ans}')