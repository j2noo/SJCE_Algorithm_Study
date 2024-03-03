arr = [[1]*15 for i in range(16)]
for i in range(1,16):
    for  j in range(1,15):
        arr[i][j]=0
        for k in range(1,j+1):
            arr[i][j]+=arr[i-1][k]
T=int(input())
for _ in range(T):
    k=int(input())  
    n=int(input())  
    print(arr[k+1][n])

# for i in range(1,15):
#     for  j in range(1,15):
#         print(arr[i][j],end=",")
#     print()