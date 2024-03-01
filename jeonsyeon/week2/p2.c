#include<stdio.h>
#include <string.h>
#include<stdlib.h>
int num(char *ch, char n){
    for(char *i=ch; i<ch+strlen(ch); i++)
       *i=(*i=='5'||*i=='6')? n=='5'?'5':'6':*i;
    return atoi(ch);
}
int main(void){
    char n1[7],n2[7];
    scanf("%s %s",n1,n2);
    printf("%d %d",num(n1,'5')+num(n2,'5'),num(n1,'6')+num(n2,'6'));                
}