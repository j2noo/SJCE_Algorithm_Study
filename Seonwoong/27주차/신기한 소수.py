import sys,math

n=int(input())

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if int(x)%i==0:
            return False
    return True

def dfs(num):
    if len(str(num))==n:
        print(num)
    else:
        for i in range(1,10,2):
            temp = num*10 +i
            if isPrime(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)
