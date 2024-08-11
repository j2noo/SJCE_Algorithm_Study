def solution(number, limit, power):
    answer = [0]+[1]*(number)
    
    cnt=0
    for i in range(2,number+1):
        for j in range(1, int(i**(1/2))+1):
            if i%j==0:
                #제곱수일 경우 예_ 4 = 2*2
                if j==i//j: 
                    cnt+=1
                #제곱수가 아닐 경우
                else:
                    cnt+=2
                    
            if cnt>limit:
                cnt=power
                break
                
        answer[i]=cnt
        cnt=0         
        
    return sum(answer)
