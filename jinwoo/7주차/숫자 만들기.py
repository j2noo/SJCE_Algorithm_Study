# li로 가장 큰 수 만들기
def solve(li):
    lastNum = -1
    while sum(li)>0:
        maxIdx = -1
        maxCnt = -1
        biggestNum = -1
        for i in range(10):
            if li[i] !=0 and lastNum !=i :
                biggestNum = i
                
            if li[i] >= maxCnt:
                maxCnt = li[i]
                maxIdx = i
        
        # 많은 숫자를 반드시 써야하는 경우
        # 13131과 같은 경우, 1을 무조건 써야함
        if maxCnt/sum(li) > 0.5:
            selectedNum = maxIdx
        else:
            selectedNum = biggestNum
            
        print(selectedNum,end="")
        li[selectedNum]-=1
        lastNum =selectedNum
            
li = list(map(int,input().split()))
length = sum(li)
maxCnt = max(li)

isAllCard = False

# 모든 카드 사용 여부 판단
if (length+1) //2 >= maxCnt : 
    isAllCard = True

# 0은 맨 앞에 올 수 없으므로, 04040과 같은 경우 제외
if length%2 ==1 and (length+1) //2 == li[0] :
    isAllCard =  False
    
# 사용 못하는 숫자는 개수를 줄이기
if isAllCard == False:
    # 0이 너무 많은 경우
    if maxCnt == li[0]:
        li[0] = max(1,sum(li[1:10]))
    # 1~9가 너무 많은 경우
    else :
        maxIdx = li.index(maxCnt)
        li[maxIdx] = sum(li)-li[maxIdx] +1
    
solve(li)