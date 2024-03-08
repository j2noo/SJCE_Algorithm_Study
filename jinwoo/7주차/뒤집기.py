str=input()

currNum='1'

# 숫자 처음과 끝이 0인 경우
if str[0]==str[-1] and str[0]=='0':
    currNum='0'
else:
    str= '1' + str + '1'
    
cnt=0
for i in range(1,len(str)):
    if str[i]!= currNum:
        cnt+=1
        currNum = '1' if currNum=='0' else '0'
        
print(cnt//2)

## str.count('01') + str.count('10')