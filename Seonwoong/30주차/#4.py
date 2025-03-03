import sys
input=sys.stdin.readline

def showActivateStr(target, check):
    answer = ""
    for i in range(len(check)):
        if check[i]:
            answer += target[i]
    return answer

target = input().strip()
check = [False] * len(target)
for i in range(len(target)):

    temp = [] 
    
    for j in range(len(check)):
        if check[j] == False:
            check[j] = True
            temp.append((showActivateStr(target, check), j))
            check[j] = False
    
    temp.sort() 
    print(temp[0][0])
    check[temp[0][1]] = True