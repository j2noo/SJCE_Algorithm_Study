# curr에 돌을 놓았을 때 끝나는지
def solve(r,c):
    color = board[r][c]
    
    # 가로
    str=''
    for i in range(-4,5):
        newR = r
        newC = c+i
        if newR<1 or newC<1 or newR >=20 or newC>=20:
            continue
        str+= board[newR][newC]
    
    if (str.count(color*5) - str.count(color*6)) ==1 :
        return 1
    
    # 새로
    str=''
    for i in range(-4,5):
        newR = r+i
        newC = c
        if newR<1 or newC<1 or newR >=20 or newC>=20:
            continue
        str+= board[newR][newC]
    
    if (str.count(color*5) - str.count(color*6)) ==1 :
        return 1
    
    
    # 5시방향
    str=''
    for i in range(-4,5):
        newR = r+i
        newC = c+i
        if newR<1 or newC<1 or newR >=20 or newC>=20:
            continue
        str+= board[newR][newC]
    
    if (str.count(color*5) - str.count(color*6)) ==1 :
        return 1
  
    # 7시방향
    
    str=''
    for i in range(-4,5):
        newR = r-i
        newC = c+i
        if newR<1 or newC<1 or newR >=20 or newC>=20:
            continue
        str+= board[newR][newC]
    
    if (str.count(color*5) - str.count(color*6)) ==1 :
        return 1
    return 0

# print("88111111".count("11111"))

N=int(input())
board = [['0']*20 for _ in range(20)]


for i in range(N):
    r,c = map(int,input().split())
    board[r][c] = str(i%2 +1)
    if solve(r,c)==1:
        print(i+1)
        exit()


# for i in range(20):
#     for j in range(20):
#         print(board[i][j],end="")
#     print()
    
    
print(-1)
