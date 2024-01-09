#include <stdio.h>
#include <string.h>

int main(void){
    char ch[100];
    int len, flag=0;
    scanf("%s",ch);
    len = strlen(ch);
    
    for(int i=0; i<len/2; i++){
        if(ch[i]!=ch[len-1-i]){
            printf("0");
            return 0;
        }
    }
    printf("1");
    return 0;
}