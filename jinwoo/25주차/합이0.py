from collections import defaultdict
n = int(input())
A,B,C,D = [],[],[],[]
INF = float("inf")
answer=0

for _ in range(n):
    input_li = list(map(int,input().split()))
    A.append(input_li[0])
    B.append(input_li[1])
    C.append(input_li[2])
    D.append(input_li[3])

sum1 = []
sum2 = defaultdict(int)
for i in range(n):
    for j in range(n):
        sum1.append(A[i]+B[j])
        sum2[C[i]+D[j]]+=1
        
for val in sum1:
    if -val in sum2:
        answer+=sum2[-val]
print(answer)
        
# sum2[-INF]=1 # F
# sum2[INF]=1 # T

# sortedSum2 = dict(sorted(sum2.items(), key=lambda x : x[0]))
# sortedKeys = list(sortedSum2.keys())
# sze = len(sortedSum2)

# # val + mid가 0보다 크거나 같은가
# def check(val1,idx):
#     val2 = sortedKeys[idx]
#     # print(f'val1, val2 : {val1,val2}')
#     if val1 + val2 >= 0:
#         return True
#     return False

# answer=0
# # sum1에서 -> sum    합이 0이 되는 수가 있는지 찾기
# for val1 in sum1:
    
#     lo,hi = 0,sze-1 # FFFTTT
#     while(lo+1<hi):
#         mid = (lo+hi)//2
        
#         if check(val1,lo) == check(val1,mid):
#             lo = mid
#         else:
#             hi = mid
#     valLo = sortedKeys[lo]
#     cntLo = sortedSum2[valLo]
    
#     valHi = sortedKeys[hi]
#     cntHi = sortedSum2[valHi]
    
#     # print(f'val1 : {val1} [{lo,hi}] , [{valLo,valHi}]\n')
#     if val1 + valLo ==0 :
#         answer+=cntLo
#     elif val1 + valHi ==0 :
#         answer+=cntHi
    
# print(sum1)
# print(sortedSum2)
# print(answer)