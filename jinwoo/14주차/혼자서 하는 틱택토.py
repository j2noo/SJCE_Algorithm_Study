# 시간 : 25분
# LV2
patterns = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
           [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],
           [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
def checkConsecutive(board,ch):
    ansFlag=False
    for cd1,cd2,cd3 in patterns:
        if board[cd1[0]][cd1[1]]==ch and board[cd2[0]][cd2[1]]==ch and board[cd3[0]][cd3[1]]==ch :
            ansFlag=True
    return ansFlag

def solution(board):
    cnt_o,cnt_x = 0,0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='O':
                cnt_o+=1
            elif board[i][j]=='X':
                cnt_x+=1
    if abs(cnt_o - cnt_x)>=2 :
        return 0
    if cnt_x > cnt_o:
        return 0
    
    is_O_consecutive = checkConsecutive(board,'O')
    is_X_consecutive = checkConsecutive(board,'X')
    
    if cnt_o == cnt_x :
        if is_O_consecutive :
            return 0
    if cnt_o == cnt_x +1:
        if is_X_consecutive :
            return 0
    return 1

# X가 더 많으면 안됨
# o,x가 2개이상 차이나면 안됨
# 1. o,x 개수가 같을 떄 -> o가 연속3개이면 안됨
# 2. o가 x보다 1개더많을때 -> x가 연속3개이면 안됨