def solve1(str1):
    day=0
    while((str1.count(')(')+str1.count('()'))>0):
        str1=str1.replace(')(','x')
        str1=str1.replace("()",'x')
        str1=str1.replace('x','')
        day+=1

    if str1!='':
        day=987654321
    return day
    

def solve2(str1):
    day=0
    while((str1.count(')(')+str1.count('()'))>0):
        str1=str1.replace("()",'x')
        str1=str1.replace(')(','x')
        str1=str1.replace('x','')
        day+=1

    if str1!='':
        day=987654321
    return day

N=int(input())
str= input()
strCpy = str

# call by value?
ans = min(solve1(str),solve2(strCpy))
if ans==987654321 :
    ans=-1
    
print(ans)

