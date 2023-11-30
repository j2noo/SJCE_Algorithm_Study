# r,c에서 크기가 size인 범위를 압축하기
def solve(r,c,size):
    if size==1:
        print(arr[r][c],end="")
        return
    
    sameFlag=1
    for i in range(r,r+size):
        for j in range(c,c+size):
            if arr[r][c] != arr[i][j]:
                sameFlag=0

    if sameFlag==0:
        print("(",end="")
        solve(r,c,size//2)
        solve(r,c+size//2,size//2)
        solve(r+size//2,c,size//2)
        solve(r+size//2,c+size//2,size//2)
        print(")",end="")
    else:
        print(arr[r][c],end="")
        
N=int(input())
arr=[list(input()) for _ in range(N)]

solve(0,0,N)