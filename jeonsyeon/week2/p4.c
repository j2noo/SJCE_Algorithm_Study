#include <stdio.h>
#include <stdlib.h>

int ar[1001],n,check[1001];

int sum(){
    int max=1; 
    for(int i=1; i<=n; i++){
        check[i]=1;
        for(int j=0; j<=i; j++){
            if(ar[j]<ar[i]&&check[i]<check[j]+1) 
                check[i] = check[j]+1;
        }
        if(max<check[i]) max=check[i];
    }
    return max;
}

int main(void){
    scanf("%d",&n);
    for(int i=0; i<n; i++) scanf("%d",&ar[i]);
    printf("%d",sum());
}