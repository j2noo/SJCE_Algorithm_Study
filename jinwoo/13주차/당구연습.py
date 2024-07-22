def solution(m, n, startX, startY, balls):
    answer = []
    
    for x,y in balls:
        ans=19231239
        # 공을 벽에 반사
        # 위
        if not (startX==x and startY<y):
            ans=min(ans,(startX-x)**2 + (n-startY + n-y)**2)
        # 아래
        if not (startX==x and startY>y):
            ans=min(ans,(startX-x)**2 + (startY + y)**2)
        # 좌
        if not (startX>x and startY==y):
            ans=min(ans,(startX + x)**2 + (startY - y)**2)
        # 우
        if not (startX<x and startY==y):
            ans=min(ans,(m-startX + m-x)**2 + ((startY -y)**2))
                    
        answer.append(ans)
    return answer
# 두 공의 x,y 가 아무것도 일치하지 않음 -> 4방향체크
# -> 1방향 정할 수 있을것같은데..? 생각안할래ccde

# x,y 하나가 일치 -> 3방향체크ssadasd