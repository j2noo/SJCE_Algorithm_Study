# 20 분
from itertools import combinations

# 1 - 모든 팀이 소수가 아닌 득점을 할 확률
# 각 팀이 [1,4,6,8,9,10,12,14,15,16,18]점을 획득할 확률
# 4골 확률
# 18C4 * (득점)^4 * (1-득점)^14

# print()
nonPrimes = [0,1,4,6,8,9,10,12,14,15,16,18]

pa = int(input()) / 100
pb = int(input()) / 100



sumA, sumB = 0,0
for np in nonPrimes :
    sumA += len(list(combinations(range(18), np))) * (pa ** np) * ((1 - pa) ** (18-np))
    sumB += len(list(combinations(range(18), np))) * (pb ** np) * ((1 - pb) ** (18-np))
    # print(f'np : {np}', len(list(combinations(range(18), np))) * (pa ** np) * ((1 - pa) ** (18-np)))
    
print(1 - (sumA * sumB))

#### 내가 3년전에 풀었던 C코드 ㅋㅋ

#include<iostream>
#include<cmath>
using namespace std;
#define ld long double
ld p1,p2;
int nCr[24][25];
void init(){
  for(int i=1;i<20;i++){
    for(int j=0;j<=i;j++){
      if(j==0 || j==i)
        nCr[i][j]=1;
      else {
        nCr[i][j]=nCr[i-1][j-1]+nCr[i-1][j];
      }
    }
  }
}
int main(){
  init();

  cin>>p1>>p2;
  p1/=100;
  p2/=100;

  ld p1sum=nCr[18][0]*pow(p1,0)*pow(1-p1,18)+
           nCr[18][1]*pow(p1,1)*pow(1-p1,17)+
           nCr[18][4]*pow(p1,4)*pow(1-p1,14)+
           nCr[18][6]*pow(p1,6)*pow(1-p1,12)+
           nCr[18][8]*pow(p1,8)*pow(1-p1,10)+
           nCr[18][9]*pow(p1,9)*pow(1-p1,9)+
           nCr[18][10]*pow(p1,10)*pow(1-p1,8)+
           nCr[18][12]*pow(p1,12)*pow(1-p1,6)+
           nCr[18][14]*pow(p1,14)*pow(1-p1,4)+
           nCr[18][15]*pow(p1,15)*pow(1-p1,3)+
           nCr[18][16]*pow(p1,16)*pow(1-p1,2)+
           nCr[18][18]*pow(p1,18)*pow(1-p1,0);
  ld p2sum=nCr[18][0]*pow(p2,0)*pow(1-p2,18)+
           nCr[18][1]*pow(p2,1)*pow(1-p2,17)+
           nCr[18][4]*pow(p2,4)*pow(1-p2,14)+
           nCr[18][6]*pow(p2,6)*pow(1-p2,12)+
           nCr[18][8]*pow(p2,8)*pow(1-p2,10)+
           nCr[18][9]*pow(p2,9)*pow(1-p2,9)+
           nCr[18][10]*pow(p2,10)*pow(1-p2,8)+
           nCr[18][12]*pow(p2,12)*pow(1-p2,6)+
           nCr[18][14]*pow(p2,14)*pow(1-p2,4)+
           nCr[18][15]*pow(p2,15)*pow(1-p2,3)+
           nCr[18][16]*pow(p2,16)*pow(1-p2,2)+
           nCr[18][18]*pow(p2,18)*pow(1-p2,0);
  printf("%8Lf",1-p1sum*p2sum);
}