# 대략20분
# lv2
from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(s,e,maps,R,C):
    v = [[0]*C for _ in range(R)]
    queue = deque()
    queue.append(s)
    v[s[0]][s[1]]=1
    
    depth=0
    while len(queue)>0:
        for _ in range(len(queue)):
            r,c = queue.popleft()
            if (r,c)==e:
                return depth
            for dir in range(4):
                nr = r + dy[dir]
                nc = c + dx[dir]
                if nr<0 or nc<0 or nr>=R or nc>=C :
                    continue
                if v[nr][nc]==0 and maps[nr][nc]!='X':
                    queue.append((nr,nc))
                    v[nr][nc]=1
        depth+=1
    return 999_999
    
def solution(maps):
    R = len(maps)
    C = len(maps[0])
    for i in range(R):
        for j in range(C):
            if maps[i][j] == 'S':
                start = (i,j)
            if maps[i][j] == 'E':
                end = (i,j)
            if maps[i][j] == 'L':
                lever = (i,j)
    answer = bfs(start,lever,maps,R,C)
    answer += bfs(lever,end,maps,R,C)
    if answer>989898:
        answer=-1
    return answer

# 시작to레버 bfs
# 레버to끝 bfs