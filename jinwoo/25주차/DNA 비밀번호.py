S,P = map(int,input().split())
st = input()
dest = list(map(int,input().split()))
cnt = [0,0,0,0]
answer=0

for idx,val in enumerate(st):
    if val == 'A':
        cnt[0]+=1
    elif val == 'C':
        cnt[1]+=1
    elif val == 'G':
        cnt[2]+=1
    elif val == 'T':
        cnt[3]+=1
        
    if idx >= P-1 :
        if idx >= P:
            if st[idx-P] == 'A':
                cnt[0]-=1
            elif st[idx-P] == 'C':
                cnt[1]-=1
            elif st[idx-P] == 'G':
                cnt[2]-=1
            elif st[idx-P] == 'T':
                cnt[3]-=1

        answerFlag=1
        for i in range(4):
            if cnt[i] < dest[i]:
                answerFlag=0
        if answerFlag ==1 :
            answer+=1
        
    
print(answer)