# 66.7 점 코드

def solution(n, l, r):
    answer = 0
    bit="1"
    for i in range(n):
        tmp=bit*2+"0"*len(bit)+bit*2
        bit=tmp
    
    for x in bit[l-1:r]:
        if x == "1": 
            answer+=1
            
    return answer


# 0 1
# 1 11011
# 2 110[11 11011 00000 11]011 11011
# 3 (11011 11011 00000 11011 11011) * 2 + [0]*len(#2) + #2 *2
# n+1 :n번째 칸토어 비트열 * 2 + 0*(n번째 칸토어 비트열 길이) + n번째 칸토어 비트열 * 2
