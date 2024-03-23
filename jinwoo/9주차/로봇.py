# 위, 오른쪽, 아래, 왼쪽 순으로 0,1,2,3
see = 1 
pos = [0,0]
M, n = map(int,input().split())


for i in range(n):
  act, val = input().split()
  val=int(val)
  # 돌기
  if act == 'TURN':
    if val== 0:
      see = (see-1) % 4
    else :
      see = (see+1) % 4
    
  # 움직이기
  else :
    if see == 0: # 위
      pos = [pos[0] + val, pos[1]]
    elif see == 1: # 오른쪽
      pos = [pos[0] , pos[1] + val]
    elif see == 2: # 아래
      pos = [pos[0] - val, pos[1]]
    elif see == 3: # 왼쪽
      pos = [pos[0] , pos[1] - val]
      
    if pos[0] <0 or pos[1] <0 or pos[1] >M or pos[0] > M:
      print(-1)
      exit()  
  # print('pos=', pos)
print(pos[1], pos[0])