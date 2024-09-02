# lv2
# 빡구현 25분
dy1 = [-1,0,1,0]
dx1 = [0,1,0,-1]

dy2 = [-1,1,1,-1]
dx2 = [1,1,-1,-1]

def isValid(r,c):ㅁ
    if r<0 or c<0 or r>=5 or c>=5 :
        return False
    return True

def solution(places):
    answer = []
    
    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                print(place[i][j], end="")
                if place[i][j]=='P':
                    # 상하좌우
                    for dir in range(4):
                        nr = i + dy1[dir]
                        nc = j + dx1[dir]
                        if not isValid(nr,nc):
                            continue
                        if place[nr][nc]=='P':
                            flag=False
                    
                    #상하좌우2칸
                    for dir in range(4):
                        nr = i + dy1[dir]*2
                        nc = j + dx1[dir]*2
                        nr_btw = i + dy1[dir]
                        nc_btw = j + dx1[dir]
                        if not isValid(nr,nc):
                            continue
                        if place[nr][nc]=='P':
                            if place[nr_btw][nc_btw]!='X':
                                flag=False
                
                    # 대각선 2칸
                    for dir in range(4):
                        nr = i + dy2[dir]
                        nc = j + dx2[dir]
                        btw1 = [i, j + dx2[dir]]
                        btw2 = [i + dy2[dir], j]
                        if not isValid(nr,nc):
                            continue
                        if place[nr][nc]=='P':
                            if place[btw1[0]][btw1[1]]!='X' or place[btw2[0]][btw2[1]]!='X':
                                    flag=False
                    
            print()
        print()
        if flag==True:
            answer.append(1)
        else :
            answer.append(0)
    return answer

# 붙어있는경우 -> X
# 2칸 직선거리 -> 파티션이 없으면 X
# 대각선 -> 파티션이 2개 없으면 X
# 모든 참여자에 대해, 8방향 검사 -> O(N*8)