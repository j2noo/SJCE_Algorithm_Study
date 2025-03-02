na,nb = map(int,input().split())

li_a = list(map(int,input().split()))
li_b = list(map(int,input().split()))

setb = set(li_b)
# print(seta)
ans = []

for la in li_a :
    if not la in setb:
        ans.append(la)
print(len(ans))
ans.sort()
if len(ans)==0 :
    exit()
for la in ans:
    print(la,end=" ")