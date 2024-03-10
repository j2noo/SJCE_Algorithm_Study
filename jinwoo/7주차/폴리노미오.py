str = input()
li = str.split('.')

ans=''
for ea in li:
    length = len(ea)
    if length % 2 ==1:
        print(-1)
        exit()
    
    for i in range(length//4):
        ans+='AAAA'
    if length%4 == 2:
        ans+='BB'
    ans+='.'
    

print(ans[0:-1])