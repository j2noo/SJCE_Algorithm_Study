# 18분
dir = {'N' : [-1,0], 'S' : [1,0],'W' : [0,-1],'E' : [0,1] }
def solution(park, routes):
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=='S':
                r,c = i,j
                
    for route in routes:
        impossibleFlag=0
        op,n =route[0],int(route[2])
        dy = dir[op][0]
        dx = dir[op][1]
        nr,nc = r,c
        for i in range(n):
            nr,nc = nr + dy, nc + dx
            if nr<0 or nc<0 or nr>=len(park) or nc >= len(park[0]) or  park[nr][nc]=='X':
                impossibleFlag=1
                break
        if impossibleFlag==0:
            r,c = nr,nc

    return [r,c]