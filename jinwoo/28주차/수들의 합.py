# 1 2 3 .. 19 = 190
# 1 2 3 ... 20 = 211
# 7분
S = int(input())

sum = 0
ans = 0
for i in range(100000):
    sum +=i
    if sum <= S :
        ans = i
        
print(ans)