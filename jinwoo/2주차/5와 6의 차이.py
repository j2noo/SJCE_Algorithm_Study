def convert(num,target,to):
    ret=0
    while(num>0):
        n=num%10
        if n==target:
            ret=ret*10+to
        else :
            ret=ret*10+n
        num=num//10
    print("@",ret)
    return ret
        

A,B = input().split()
maxA = A.replace('5','6')
minA = A.replace('6','5')
maxB = B.replace('5','6')
minB = B.replace('6','5')

print(int(minA)+int(minB),end=" ")
print(int(maxA)+int(maxB),)
