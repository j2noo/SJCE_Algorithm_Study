# def solve1(str1):
#     day=0
#     while(True):
#         beforeLen = len(str1)
#         str1=str1.replace(')(','x')
#         str1=str1.replace("()",'x')
#         str1=str1.replace('x','')
#         afterLen = len(str1)
#         if beforeLen == afterLen :
#             break
#         day+=1

#     if str1!='':
#         day=987654321
#     return day
    

# def solve2(str1):
#     day=0
#     while(True):
#         beforeLen = len(str1)
#         str1=str1.replace("()",'x')
#         str1=str1.replace(')(','x')
#         str1=str1.replace('x','')
#         afterLen = len(str1)
#         if beforeLen == afterLen :
#             break
#         day+=1

#     if str1!='':
#         day=987654321
#     return day

N=int(input())
str= input()
strCpy = str

day=0
while(True):
    
    beforeLen = len(str)
    prev = 'z'
    newStr = ''
    for i in range(len(str)):
        if prev=='(':
            if str[i] ==')':
                prev='x'
            else :
                newStr+=prev
                prev = str[i]
                
        elif prev==')':
            if str[i] =='(':
                prev='x'
            else :
                newStr+=prev
                prev = str[i]
        else :
            prev = str[i]
            # newStr+=prev  !!
    afterLen = len(newStr)
    str= newStr 
    day+=1
    if beforeLen == afterLen :
        break
    day2=0
while(True):
    beforeLen = len(strCpy)
    prev = 'z'
    newStr = ''
    for i in range(len(strCpy)):
        if prev==')':
            if strCpy[i] =='(':
                prev='x'
            else :
                newStr+=prev
                prev = strCpy[i]
                
        elif prev=='(':
            if strCpy[i] ==')':
                prev='x'
            else :
                newStr+=prev
                prev = strCpy[i]
        else :
            prev = strCpy[i]
            # newStr+=prev  !
    afterLen = len(newStr)
    strCpy= newStr 
    day2+=1
    if beforeLen == afterLen :
        break
   
print(day,day2,str)    

# if ans==987654321 :
#     ans=-1
    


