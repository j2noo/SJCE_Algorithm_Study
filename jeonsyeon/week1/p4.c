#include <stdio.h>
 
int d[1001];
int main(void)
{
    int n;
    d[0]=d[1]=1;
    scanf("%d",&n);
    for (int i=2;i<=n;i++) d[i]=(d[i-1]+d[i-2])%10007;
    printf("%d",d[n]);
}
