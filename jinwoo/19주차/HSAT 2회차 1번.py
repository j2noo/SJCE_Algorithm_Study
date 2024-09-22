# 43분 
def calcArea(x1,y1,x2,y2):
    return abs(x1-x2) * abs(y1-y2)
import sys
x_dic = {} # x좌표로 정사영시 어떤 색의 점이 존재하는지
for idx in range(-1000,1001):
    x_dic[idx]=[]
point_li = []
COLOR_CNT = -1
N,K = map(int,input().split())
for _ in range(N):
    x,y,color = map(int,input().split())
    COLOR_CNT = max(COLOR_CNT,color) # 전체 색의 수
    point_li.append((x,y,color))
    x_dic[x].append(color) # 중복 색 제거?

# for i in range(-10,11):
#     print(i,x_dic[i])
# print(point_li)
# print("colorCNT : ",COLOR_CNT)
ans = float("inf")
# 두 점을 고르고, 두 점 내부에 모든 색이 존재하는지 파악
for i in range(N):
    for j in range(i+1,N):
        isColored = [0]*(COLOR_CNT+1)
        isColored[0]=1
        x1,y1,color1 = point_li[i] # 점1
        x2,y2,color2 = point_li[j] # 점2
        # print(x1,"to ",x2,"@")
        start,end = min(x1,x2), max(x1,x2) # 두 점의 x좌표
        for x in range(start,end+1):
            for x_color in x_dic[x]:
                isColored[x_color]=1
                # print("발견",x_color)
        # 모든 색이 칠해졌는지 체크
        if 0 in isColored:
            continue
        area = calcArea(x1,y1,x2,y2)   
        ans = min(ans,area)
print(ans)




# 직사각형이 비스듬할 수 있나? X
# 점은최대 100개, 색은 20개
# 모든 사각형 : 
# 2000 * 2000

# x좌표가 포함되는 경우를 전부 구하면 y좌표는 결정된다.
# 100C2로 두 점을 구한다. 점 내부에 모든 색이 존재하는지 판별한다.
    # -> 위 과정을 위해, x인덱스배열에 점 색을 넣자.