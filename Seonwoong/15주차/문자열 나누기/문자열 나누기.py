def solution(s):
    cnt1,cnt2=0,0
    answer=0
    for i in range(len(s)):
        # 문자 x 추출
        if cnt1==0 and cnt2==0: x=s[i]
        
        # x이면 cnt1증가, x아닌 문자 cnt2증가
        if s[i]==x: cnt1+=1
        else: cnt2+=1
            
        # 두 횟수가 같아지는 순간, 정답 카운트 증가, 변수 초기화
        if cnt1==cnt2:
            answer+=1
            cnt1,cnt2=0,0
            
        # 더 읽을 글자가 없다면 정답 카운트 증가
        if i==len(s)-1 and cnt1>0: answer+=1
        
    return answer
