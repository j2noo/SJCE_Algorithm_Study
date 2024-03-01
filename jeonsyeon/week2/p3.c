#include<stdio.h>

char ar[64][64];

void quad(int a, int b, int size){
    for(int i=0; i<size; i++){
        for(int j=0; j<size; j++){
            if(ar[a+i][b+j]!=ar[a][b]) goto false;
        }
    }
    printf("%c",ar[a][b]);
    return;

    false: printf("(");
    quad(a,b,size/2);quad(a,b+size/2,size/2);
    quad(a+size/2,b,size/2);quad(a+size/2,b+size/2,size/2);
    printf(")");
    return ;
}

int main(void){
    int n;
    scanf("%d",&n);
    for(int i=0; i<n; i++) scanf("%s",ar[i]);
    quad(0,0,n);
}