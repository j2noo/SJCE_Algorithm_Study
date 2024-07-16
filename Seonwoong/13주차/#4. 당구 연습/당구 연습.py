def d(x1,y1, x2,y2):
    return (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)

def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        x,y=ball
        #x,y 좌표를 x축 대칭, y축 대칭, x=m 대칭, y=n대칭 시킨 좌표와 시작점의 거리 계산
        if x!= startX and y!=startY:
            answer.append(min(d(startX,startY,x,2*n-y),d(startX,startY,x,-y),d(startX,startY,-x,y),d(startX,startY,2*m-x,y)))
        
        elif y==startY:
            if startX>x: 
                # 입출력 예시 2: x=m 대칭이동, y=n, x축 대칭이동 
                answer.append(min(d(startX,startY,2*m-x,y),d(startX,startY,x,startY+min(2*y, 2*n-2*y))))
            else: 
                # 입출력 예시 1: x=0 대칭이동, y=n, x축 대칭이동
                answer.append(min(d(-startX,startY,x,y),d(startX,startY,x,startY+min(2*y, 2*n-2*y))))
        
        # 위와 대칭..
        elif x==startX:
            if startY>y:            
                answer.append(min(d(startX,startY,x,2*n-y),d(startX,startY,startX+min(2*x,2*m-2*x),y)))
            else:
                answer.append(min(d(startX,-startY,x,y),d(startX,startY,startX+min(2*x,2*m-2*x),y)))
                
    return answer

# 수학 문제?
# 9분
