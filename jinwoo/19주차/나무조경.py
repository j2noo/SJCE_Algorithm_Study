# LV3
# 38분
COORD = [(0,0),(0,1),(0,2),(0,3),
        (1,0),(1,1),(1,2),(1,3),
        (2,0),(2,1),(2,2),(2,3),
        (3,0),(3,1),(3,2),(3,3)]
pair = [(0,1),(1,2),(2,3),
       (4,5),(5,6),(6,7),
       (8,9),(9,10),(10,11),
       (12,13),(13,14),(14,15),
       #
       (0,4),(4,8),(8,12),
       (1,5),(5,9),(9,13),
       (2,6),(6,10),(10,14),
       (3,7),(7,11),(11,15)]
import sys
import itertools


# 모든 입력값을 4*4로 맞춤
arr = [[-9999]*4 for _ in range(4)]
n = int(input())
for i in range(n):
    input_li = list(map(int,input().split()))
    for j in range(len(input_li)):
        arr[i][j]= input_li[j]
        
# for i in range(4):
#     print(arr[i])

# 완탐 시작
ans=0
comb_li = list(itertools.combinations(range(24),4))
comb_li += list(itertools.combinations(range(24),3))
comb_li += list(itertools.combinations(range(24),2))
for comb in comb_li:
    psum=0
    isSelected = [0]*16
    duplicateFlag = False
    for idx in comb:
        idx1,idx2 = pair[idx]
        coord1, coord2 = COORD[idx1],COORD[idx2]
        isSelected[idx1] +=1
        isSelected[idx2] +=1
        psum+=arr[coord1[0]][coord1[1]]
        psum+=arr[coord2[0]][coord2[1]]
        
    for item in isSelected:
        if item>1 :
            duplicateFlag=True
    if  duplicateFlag:
        continue
    # print(comb)
    ans=max(ans,psum)
print(ans)

# 4 by 4
# 16C2 * 14C2 * 12C2 *10C2 = 6천만 -> 완탐
# 가능한 쌍 : 가로12 + 세로12 = 24, 24C4