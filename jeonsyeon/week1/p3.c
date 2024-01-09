#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b) {
    int tmp = *a;*a = *b;*b = tmp;
}

void min(int arr[],int n) {
    for (int i = n - 1; i > 0; i--)
        for (int j = 0; j < i; j++)
            if (arr[j] > arr[j + 1])
                swap(&arr[j], &arr[j + 1]);
}
void max(int arr[],int n) {
    for (int i = n - 1; i > 0; i--)
        for (int j = 0; j < i; j++)
            if (arr[j] < arr[j + 1])
                swap(&arr[j], &arr[j + 1]);
}

int main(void){

    int cnt=0,*a,*b,n;
    scanf("%d",&n);
    a = (int*)calloc(n,sizeof(int));
    b = (int*)calloc(n,sizeof(int));
    for(int i=0; i<n; i++)scanf("%d",&a[i]);
    for(int i=0; i<n; i++)scanf("%d",&b[i]);
    
    min(a,n),max(b,n);

    for(int i=0; i<n; i++) cnt += a[i]*b[i];

    printf("%d",cnt);
}