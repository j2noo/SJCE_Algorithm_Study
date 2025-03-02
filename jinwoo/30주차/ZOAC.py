# A
# ZA, OA, AC -> AC
# ZAAC, OAC

#BAC
# A
# BA, AC -> AC

# 100번 -> 100*100 정렬 브루트포스
strs = input()
N = len(strs)
isOpen = [0]*N # 공개 여부

def xor(a,b):
    return (a and not(b)) or (b and not(a)) 

for length in range(1,N+1):
    li = [] # list(문자열, 추가된idx)
    
    # idx번째가 추가된다고 가정하고문자열 만들어보기
    for idx in range(N):
        
        tmpStr = ''
        for i in range(N):
            if xor(isOpen[i]==1, i == idx) : 
                tmpStr += strs[i]
        if len(tmpStr) == length:
            li.append([tmpStr,idx])
        
    li.sort()
    isOpen[li[0][1]] = 1 # 선택됨
    print(li[0][0])
    
    