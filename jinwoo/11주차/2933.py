import sys
sys.setrecursionlimit(10**5)
dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 땅에서 떨어진 클러스터 찾기
def dfs(r,c):
    global v
    global isOnAir
    v[r][c]=1
    
    # 땅이랑 연결된 미네랄임
    if r==R-1:
        isOnAir=0
        return
    
    for dir in range(4):
        nr = r+dy[dir]
        nc = c+dx[dir]
        if  isValid(nr,nc) and arr[nr][nc]=='x' and v[nr][nc]==0:
            dfs(nr,nc)
    

# 아래로 내리기 위한 함수
# r,c가 포함된 클러스터가 공중에 존재함.
def down(r,c):
    global v
    maxHeight = -123123
    v = [[0]*C for _ in range(R)]
    # o로 변환
    dfsTrans(r,c)
    
    # 한칸씩 내리며 땅 또는 x를 만나면 그만
    o_li = [] # 한칸씩내리기
    for r in range(R):
        for c in range(C):
            if arr[r][c] =='o':
                o_li.append([r,c])
    
    for height in range(1,R):
        flag=1
        for o_r,o_c in o_li:
            nr = o_r+height
            nc=o_c

            #한칸 아래가 x거나 땅이면
            if nr==R-1 or (isValid(nr+1,nc) and arr[nr+1][nc]=='x'  ):
                flag=0
                break
        if flag==0:
            maxHeight = height
            break

    o_li = []
    trans_li = []
    for r in range(R):
        for c in range(C):
            if arr[r][c]=='o':
                o_li.append([r,c])
                trans_li.append([r+maxHeight,c])
               
    for o_r,o_c in o_li :
        arr[o_r][o_c]='.'
    for trans_r,trans_c in trans_li :
        arr[trans_r][trans_c]='x'
        
    

def dfsTrans(r,c):
    global v
    v[r][c]=1
    arr[r][c]='o'
    for dir in range(4):
        nr = r+dy[dir]
        nc = c+dx[dir]
        if  isValid(nr,nc) and arr[nr][nc]=='x'  and v[nr][nc]==0:
            dfsTrans(nr,nc)

def isValid(r,c):
    return r>=0 and c>=0 and r<R and c<C
    
stick_dist = [1,-1] # 막대기 진행 방향

R,C = map(int,input().split())
arr = []
for _ in range(R):
    arr.append(list(input()))
N = int(input())
height_li = list(map(int,input().split()))

v = [[0]*C for _ in range(R)]


# 부순 미네랄 위치 파악
for i in range(len(height_li)):
    h=height_li[i]
    
    # 막대기의 진행 방향
    dist = stick_dist[i%2]
    findR = R-h
    # 왼->오
    if i%2 ==0:
        findC = 0
    else:
        findC = C-1
    
    mineral = arr[findR][findC]
    while mineral=='.' :
        findC = findC + dist
        if findC<0 or findC>=C:
            break
        mineral = arr[findR][findC]
    
    # R,C 미네랄 찾음
    
    # 미네랄이 존재X -> 그냥 넘어감
    if findC<0 or findC>=C:
        continue
    # print('find r,c:',findR,findC)
    
    
    # 찾은 미네랄의 좌우가 없는데, 바로 위에 존재하는경우
    # 찾은 미네랄의 좌우상을 dfs했을떄,아래가 비는경우(가장 높은 높이 찾기)
    arr[findR][findC] = '.'

    # 공중에 떠 있는 클러스터 먼저 찾기
    v = [[0]*C for _ in range(R)]
    
    isOnAir=1
    airFlag=0
    for r in range(R):
        for c in range(C):
            if v[r][c]==0 and arr[r][c]=='x' and airFlag==0:
                isOnAir=1
          
                dfs(r,c)
                if isOnAir==1 :
                    down(r,c)
                    airFlag=1
                    break

for r in range(R):
    for c in range(C):
        print(arr[r][c],end="")
    print()
    
    

    