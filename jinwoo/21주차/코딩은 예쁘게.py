# 1시간
# 골3
N = int(input())
cur_li = list(map(int,input().split()))
goal_li = list(map(int,input().split()))

diff_li = []
for i in range(N):
    diff_li.append(cur_li[i] - goal_li[i])
    
answer = 0

# 더하기 먼저 수행(diff가 음수 인 경우)
# 0이 아닌, [l,r] 구간을 찾음
while(True):
    l,r = -1,-1
    for idx, diff in enumerate(diff_li):
        if l==-1 and diff < 0:
            l = idx
        if diff < 0 :
            r = idx
            
    # 구간 내에 음수가 없음
    if r == -1 :
        break
            
    # 제일 적게 더하는 탭 찾기
    min_tap = 999
    for idx in range(l,r+1):
        if diff_li[idx] < 0 :
            min_tap = min(min_tap, abs(diff_li[idx]))
    
    # 탭 쳐주기
    for idx in range(l,r+1):
        diff_li[idx] +=min_tap
    answer += min_tap

# 빼기수행(diff가 양수 인 경우)
# 0이 아닌, [l,r] 구간을 찾음+ 0이 포함되면 안됨
while(True):
    l,r = -1,-1
    for idx, diff in enumerate(diff_li):
        # diff가 0인경우
        if diff == 0 :
            if r ==-1 : # 아직 구간 탐색이 안된경우 진행
                continue
            else : # 구간을 찾은경우 해당 구간에 대해 탭 빼기 진행
                break
        if l==-1 and diff > 0:
            l = idx
        if diff > 0 :
            r = idx
            
    # 모든 diff가 0이 됨
    if r == -1 :
        break
    
    # 제일 적게 빼는  탭 찾기
    min_tap = 999
    for idx in range(l,r+1):
        if diff_li[idx] > 0 :
            min_tap = min(min_tap, abs(diff_li[idx]))
            
    # 탭 빼주기
    for idx in range(l,r+1):
        diff_li[idx] -=min_tap
    answer += min_tap
    
print(answer)

# ----> 잘못된 접근 1
# 음/양이 연속해서 나오는 경우
# 무조건 두 절댓값의 합인가? 아닌 경우가 없나?
# -50 2 -50 3 -> 102+3
# 같은부호 -> 가장 큰 값, 다른부호 -> 절대값 

##### -> 접근2
# 음수 먼저 체크한다.(탭을 쳐야하는 경우)
# [l,r] 구간에서 가장 작은 수를 찾아서 그만큼 tap을 쳐 준다. 
# 구간에서 사이드에 발생하는 0은 제외한다.
# 4 3 0 3 처럼 중간에 0이 끼는 경우는 포함해서 tap을 쳐 준다.
# 왜냐하면 양수(탭을 제거하는 경우)에서 제거하는 과정이 있으므로 횟수가 동일함

# 그 다음 음수 체크(탭을 제거하는 경우)
# [l,r] 구간에서 가장 작은 수를 찾아서 그만큼 tap을 뺀다.
# 탭을 치는 것과 다르게, 중간에 0이 있으면 안되므로 구간에 0을 포함하지 않고 한다.
