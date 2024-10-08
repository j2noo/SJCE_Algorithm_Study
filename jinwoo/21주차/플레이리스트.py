# P개에  N개를 배열 -> 최대 100!,  P!
# 첫 노래 : 전부
# 두번쨰 노래 : 첫번쨰노래 * (N-1)개 종류로 길이가 M-1인 노래

# N개의 노래가 존재하고, 같은노래 사이에 M=2개가 있어야함
# 첫번쨰 노래 : N가지 
# 두번째 노래 : N*N-1 
# 세번쨰 노래 : N *N-1 * N-2
# 네번쨰 노래1: 첫번째노래 * (N-1)종류로 길이가M인 노래 가짓수 * (N-M)

import itertools
MOD = 1_000_000_007

# idx번째 까지 N개의 노래로 중복없이 채워야 함
def permutation(N,idx):
    ret =1
    for i in range(idx):
        ret*=(N-i)
        ret %=MOD
    return ret

N,M,P = map(int,input().split())
dp = [-1] * 101
dp[0] = 1

# M+1개 노래까지는 중복 제한이 없음
for i in range(1,M+2):
    dp[i] = permutation(N,i)
print(dp)
print("@")

# M+2번쨰 노래
for i in range(M+2, 101):
    dp[i] = dp[i - (M+1)] * dp[M] * (N-M)
    dp[i] %=MOD

print(dp)
print(dp[P])