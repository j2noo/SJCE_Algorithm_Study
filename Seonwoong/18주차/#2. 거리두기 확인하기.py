def check(places):
    for i in range(5):
        for j in range(5):
            # 자리가 붙어있는 경우
            if places[i][j]=='P':
                if i>=1 and places[i-1][j]=='P': return 0
                if j>=1 and places[i][j-1]=='P': return 0
                if j<4 and places[i][j+1]=='P': return 0
                if i<4 and places[i+1][j]=='P': return 0 

            cnt=0
            # POP 느낌 테이블 주위에 자리가 두개 이상 있는 경우
            if places[i][j]=='O':
                if i>=1 and places[i-1][j]=='P': cnt+=1
                if j>=1 and places[i][j-1]=='P': cnt+=1
                if j<4 and places[i][j+1]=='P': cnt+=1
                if i<4 and places[i+1][j]=='P': cnt+=1

                if cnt>1: return 0

    else:
        return 1

def solution(places):
    answer = []
    for i in range(len(places)):
        answer.append(check(places[i]))
    return answer
