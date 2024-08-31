def solution(park, routes):
    answer=[]
    #시작점 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=='S':
                sx,sy=i,j
                break
               
    op=[[-1,0],[0,1],[0,-1],[1,0]] #NEWS
    #방향 설정: 반대 주의
    
    #시간복잡도 O(kn): 최대 450개 k: 1~9(실제 n값), n: 1~50(routes 길이)
    for route in routes:
        news,n=route.split(' ')
        n=int(n)
        nx,ny=sx,sy
        
        if news=='N': idx=0
        elif news=='E': idx=1
        elif news=='W':idx=2
        else: idx=3

        #route에 X가 있는지 한칸씩 확인
        for i in range(n):
            dx,dy=op[idx][0],op[idx][1]
            if 0<=sx+dx<len(park) and 0<=sy+dy<len(park[0]) and park[sx+dx][sy+dy]!='X':
                sx,sy=sx+dx,sy+dy
            else:
                sx,sy=nx,ny
                break
                
    answer.append([sx,sy])  

    return answer[0]
