# 1시간 ㅅ..abs
# answer=[-1]
maxGap = 0
lowerArrowScore= -1 # 낮은 과녁 점수
arrows = [0] * 11 # 라이언이 꽂은 과녁 점수
def calcArrowScore(lions):
    lions = lions[::-1]
    sum = 0
    for idx, val in enumerate(lions):
        sum += val * (11**idx)
    return sum

def calc(lions,peachs):
    global maxGap, answer,lowerArrowScore
    score_lion,score_peach = 0,0
    for i in range(1,11):
        if lions[i] > peachs[i] :
            score_lion+= i
        elif lions[i] <= peachs[i] and peachs[i]>0:
            score_peach+=i
    gap = score_lion - score_peach
    
    if gap >0 and gap >= maxGap:
        answer = lions[:]
        maxGap = score_lion - score_peach
        lowerArrowScore = calcArrowScore(lions)
        
    # elif gap >0 and gap == maxGap:
    #     currentLowerArrowScore = calcArrowScore(lions)
    #     # if currentLowerArrowScore < lowerArrowScore :
    #     answer = lions[:]
    #     lowerArrowScore =currentLowerArrowScore
    #     # print(f'lion : {score_lion},apeach : {score_peach} ',lions)
        
        
def solution(n, info):
    global answer
    info = info[::-1]
    # score점수에, left개 화살이 남았을때 꽂는 경우의 수
    def dfs(score,left):
        if score == 10 :
            arrows[10]=left
            calc(arrows,info)
            return
        
        for i in range(left+1):
            arrows[score] = i
            dfs(score+1,left-i)
            arrows[score]=0
            
    dfs(0,n)
    return answer[::-1]

# 어피치가 맞힌 곳을 무조건 맞춰야하는가? -> 모름 -> 완탐
# 10^10 = 10,000,000,000 x
# 10개 중에, 중복 허용 10개를 고르기 10H10 = 19C10 = 9만 dp?