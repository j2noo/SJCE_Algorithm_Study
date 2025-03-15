# dfs? with 방문지도
dy = [0,1,0,-1]
dx = [1,0,-1,0]
ans = 987654321
def dfs(r,c,cnt):
    global ans
    global isVisited
    print(f'{r},{c},{cnt}')


    if cnt >= ans :
        return 
    # if cnt + (N-r) + (M-c) > ans :
    #     return 
    if r == N-1 and c == M-1 :
        ans = min(ans,cnt)
    # print(f'{r},{c},{cnt}')

        return
        
    for dir in range(4):
        nr = r + dy[dir]
        nc = c + dx[dir]
        if nr <0 or nr>= N or nc <0 or nc>= M:
            continue
        if isVisited[nr][nc] == 1 : 
            continue
        
        isVisited[nr][nc] = 1
        if arr[nr][nc] == '0' :

            dfs(nr,nc,cnt)
        else : 

            dfs(nr,nc,cnt+1)
        isVisited[nr][nc] = 0


M,N  = map(int,input().split())
isVisited = [[0]*M for _ in range(N)]

arr = []
for _ in range(N):
    arr.append(list(input()))

# print(arr)

dfs(0,0,0)
print(ans)